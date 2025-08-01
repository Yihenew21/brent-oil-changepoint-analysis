import pymc3 as pm
import numpy as np
import pandas as pd
from typing import Tuple
import matplotlib.pyplot as plt
from pathlib import Path

def build_changepoint_model(data: np.ndarray, n_days: int) -> pm.Model:
    """
    Build a Bayesian change point model with a single switch point for time series data.

    Args:
        data (np.ndarray): Array of observed data (e.g., Brent oil prices or log returns).
        n_days (int): Number of time points in the data.

    Returns:
        pm.Model: PyMC3 model with defined priors, switch point, and likelihood.
    """
    # Initialize PyMC3 model
    with pm.Model() as model:
        # Define prior for switch point (tau) as discrete uniform over all days
        tau = pm.DiscreteUniform("tau", lower=0, upper=n_days - 1)

        # Define priors for mean before and after the switch point
        mu_1 = pm.Normal("mu_1", mu=np.mean(data), sd=np.std(data))
        mu_2 = pm.Normal("mu_2", mu=np.mean(data), sd=np.std(data))

        # Define prior for standard deviation (shared for simplicity)
        sigma = pm.HalfNormal("sigma", sd=np.std(data))

        # Use switch function to select mean based on time index
        mu = pm.math.switch(tau >= np.arange(n_days), mu_1, mu_2)

        # Define likelihood: observed data follows normal distribution
        observation = pm.Normal("obs", mu=mu, sd=sigma, observed=data)

    return model

def run_mcmc(model: pm.Model, draws: int = 1000, tune: int = 1000) -> pm.backends.base.MultiTrace:
    """
    Run MCMC sampling to estimate posterior distributions.

    Args:
        model (pm.Model): PyMC3 model to sample from.
        draws (int): Number of posterior samples to draw.
        tune (int): Number of tuning samples.

    Returns:
        pm.backends.base.MultiTrace: MCMC trace containing posterior samples.
    """
    # Run MCMC sampling
    with model:
        trace = pm.sample(draws=draws, tune=tune, return_inferencedata=False)

    return trace

def plot_changepoint_results(trace: pm.backends.base.MultiTrace, data: np.ndarray, dates: pd.Series, output_path: str) -> None:
    """
    Plot posterior distributions and data with estimated change point.

    Args:
        trace (pm.backends.base.MultiTrace): MCMC trace with posterior samples.
        data (np.ndarray): Observed data (e.g., Brent oil prices).
        dates (pd.Series): Corresponding dates for the data.
        output_path (str): Path to save the plot.

    Returns:
        None: Saves plot to output_path.
    """
    # Create figure with two subplots
    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(12, 10))

    # Plot data with mean change point
    ax1.plot(dates, data, label="Brent Oil Price", color="blue")
    tau_samples = trace["tau"]
    tau_mean = int(np.mean(tau_samples))
    ax1.axvline(dates.iloc[tau_mean], color="red", linestyle="--", label=f"Mean Change Point: {dates.iloc[tau_mean].date()}")
    ax1.set_title("Brent Oil Prices with Estimated Change Point")
    ax1.set_xlabel("Date")
    ax1.set_ylabel("Price (USD/barrel)")
    ax1.legend()
    ax1.grid(True)

    # Plot posterior distribution of tau
    ax2.hist(tau_samples, bins=50, density=True, alpha=0.7, color="purple")
    ax2.set_title("Posterior Distribution of Change Point (tau)")
    ax2.set_xlabel("Day Index")
    ax2.set_ylabel("Density")
    ax2.grid(True)

    # Adjust layout and save plot
    plt.tight_layout()
    Path(output_path).parent.mkdir(parents=True, exist_ok=True)
    plt.savefig(output_path)
    plt.close()

def interpret_changepoint(trace: pm.backends.base.MultiTrace, dates: pd.Series, events_df: pd.DataFrame) -> dict:
    """
    Interpret change point results by associating with events and quantifying impact.

    Args:
        trace (pm.backends.base.MultiTrace): MCMC trace with posterior samples.
        dates (pd.Series): Dates corresponding to data.
        events_df (pd.DataFrame): DataFrame with events (columns: 'Start Date', 'Event Name', etc.).

    Returns:
        dict: Dictionary with change point date, associated event, and price impact.
    """
    # Get mean change point index and date
    tau_mean = int(np.mean(trace["tau"]))
    change_date = dates.iloc[tau_mean]

    # Find closest event within 30 days
    events_df["Start Date"] = pd.to_datetime(events_df["Start Date"])
    time_diffs = np.abs((events_df["Start Date"] - change_date).dt.days)
    closest_event_idx = time_diffs.idxmin()
    closest_event = events_df.iloc[closest_event_idx]

    # Quantify impact: difference in mean prices before/after
    mu_1_mean = np.mean(trace["mu_1"])
    mu_2_mean = np.mean(trace["mu_2"])
    price_change = mu_2_mean - mu_1_mean
    percent_change = (price_change / mu_1_mean) * 100

    return {
        "change_point_date": change_date.date(),
        "associated_event": closest_event["Event Name"],
        "event_date": closest_event["Start Date"].date(),
        "event_description": closest_event["Description"],
        "price_change_usd": round(price_change, 2),
        "percent_change": round(percent_change, 2)
    }