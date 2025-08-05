import pymc as pm
import numpy as np
import pandas as pd
from typing import Tuple
import matplotlib.pyplot as plt
from pathlib import Path
import arviz as az


def build_changepoint_model(data: np.ndarray, n_days: int) -> pm.Model:
    """
    Build a Bayesian change point model with a single switch point for time series data.

    Args:
        data (np.ndarray): Array of observed data (e.g., log returns of Brent oil prices).
        n_days (int): Number of time points in the data.

    Returns:
        pm.Model: PyMC model with defined priors, switch point, and likelihood.
    """
    with pm.Model() as model:
        # Define prior for switch point (tau) as categorical over reduced points
        tau_idx = pm.Categorical("tau_idx", p=np.ones(n_days // 20) / (n_days // 20))
        tau = pm.Deterministic("tau", tau_idx * 20)

        # Define priors for mean before and after the switch point
        mu_1 = pm.Normal("mu_1", mu=0, sigma=np.std(data))
        mu_2 = pm.Normal("mu_2", mu=0, sigma=np.std(data))

        # Define prior for standard deviation
        sigma = pm.HalfNormal("sigma", sigma=np.std(data))

        # Use switch function to select mean based on time index
        mu = pm.math.switch(tau >= np.arange(n_days), mu_1, mu_2)

        # Define likelihood
        observation = pm.Normal("obs", mu=mu, sigma=sigma, observed=data)

    return model


def run_mcmc(
    model: pm.Model, n_days: int, data: np.ndarray, draws: int = 250, tune: int = 5000
) -> az.InferenceData:
    """
    Run MCMC sampling to estimate posterior distributions.

    Args:
        model (pm.Model): PyMC model to sample from.
        n_days (int): Number of time points in the data.
        data (np.ndarray): Observed data used to build the model.
        draws (int): Number of posterior samples to draw.
        tune (int): Number of tuning samples.

    Returns:
        az.InferenceData: MCMC posterior samples in ArviZ format.
    """
    with model:
        # Use hybrid sampler: Metropolis for tau_idx, NUTS for others
        step1 = pm.Metropolis(vars=[model.tau_idx])
        step2 = pm.NUTS(vars=[model.mu_1, model.mu_2, model.sigma])
        step = pm.CompoundStep([step1, step2])
        # Run sampling with initialization
        initvals = {
            "tau_idx": n_days // 40,
            "mu_1": np.mean(data[: n_days // 2]),
            "mu_2": np.mean(data[n_days // 2 :]),
            "sigma": np.std(data),
        }
        trace = pm.sample(
            draws=draws,
            tune=tune,
            chains=4,
            step=step,
            initvals=initvals,
            target_accept=0.95,
            return_inferencedata=True,
            progressbar=True,
        )

    return trace


def plot_changepoint_results(
    trace: az.InferenceData, data: np.ndarray, dates: pd.Series, output_path: str
) -> None:
    """
    Plot posterior distributions and data with estimated change point.

    Args:
        trace (az.InferenceData): MCMC trace with posterior samples.
        data (np.ndarray): Observed data (e.g., log returns).
        dates (pd.Series): Corresponding dates for the data.
        output_path (str): Path to save the plot.

    Returns:
        None: Saves plot to output_path.
    """
    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(12, 10))

    # Extract tau samples from InferenceData
    tau_samples = trace.posterior["tau"].values.flatten()
    tau_mean = int(np.mean(tau_samples))

    # Plot data with mean change point
    ax1.plot(dates, data, label="Log Returns", color="blue")
    ax1.axvline(
        dates.iloc[tau_mean],
        color="red",
        linestyle="--",
        label=f"Mean Change Point: {dates.iloc[tau_mean].date()}",
    )
    ax1.set_title("Log Returns of Brent Oil Prices with Estimated Change Point")
    ax1.set_xlabel("Date")
    ax1.set_ylabel("Log Returns")
    ax1.legend()
    ax1.grid(True)

    # Plot posterior distribution of tau
    ax2.hist(tau_samples, bins=50, density=True, alpha=0.7, color="purple")
    ax2.set_title("Posterior Distribution of Change Point (tau)")
    ax2.set_xlabel("Week Index")
    ax2.set_ylabel("Density")
    ax2.grid(True)

    plt.tight_layout()
    Path(output_path).parent.mkdir(parents=True, exist_ok=True)
    plt.savefig(output_path)
    plt.close()


def interpret_changepoint(
    trace: az.InferenceData, dates: pd.Series, events_df: pd.DataFrame
) -> dict:
    """
    Interpret change point results by associating with events and quantifying impact.

    Args:
        trace (az.InferenceData): MCMC trace with posterior samples.
        dates (pd.Series): Dates corresponding to data.
        events_df (pd.DataFrame): DataFrame with events (columns: 'Start Date', 'Event Name', etc.).

    Returns:
        dict: Dictionary with change point date, associated event, and impact on log returns.
    """
    tau_samples = trace.posterior["tau"].values.flatten()
    tau_mean = int(np.mean(tau_samples))
    change_date = dates.iloc[tau_mean]

    events_df["Start Date"] = pd.to_datetime(events_df["Start Date"])
    time_diffs = np.abs((events_df["Start Date"] - change_date).dt.days)
    closest_event_idx = time_diffs.idxmin()
    closest_event = events_df.iloc[closest_event_idx]

    mu_1_mean = np.mean(trace.posterior["mu_1"].values)
    mu_2_mean = np.mean(trace.posterior["mu_2"].values)
    return_change = mu_2_mean - mu_1_mean

    return {
        "change_point_date": change_date.date(),
        "associated_event": closest_event["Event Name"],
        "event_date": closest_event["Start Date"].date(),
        "event_description": closest_event["Description"],
        "log_return_change": round(return_change, 4),
    }
