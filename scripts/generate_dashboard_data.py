"""Generate and save data for the dashboard, including prices and change point results."""

import pandas as pd
import numpy as np

# Add the project root directory
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from src.models.changepoint_model import (
    build_changepoint_model,
    run_mcmc,
    interpret_changepoint,
)
from pathlib import Path
import json


def generate_dashboard_data():
    """Generate and save data for the dashboard, including prices and change point results.

    Returns:
        None: Saves data to 'dashboard/backend/data.json'.
    """
    # Load preprocessed data
    price_df = pd.read_csv("data/processed/cleaned_oil_data.csv", parse_dates=["Date"])
    events_df = pd.read_csv("data/events/major_events.csv", quotechar='"', quoting=1)

    # Prepare data for modeling (weekly downsampling)
    model_df = price_df.dropna(subset=["Log_Returns"])
    model_df = model_df.resample("W", on="Date").mean().reset_index()
    log_returns = model_df["Log_Returns"].values
    dates = model_df["Date"]
    n_days = len(log_returns)

    # Build and run model with optimized parameters
    model = build_changepoint_model(log_returns, n_days)
    trace = run_mcmc(model, n_days, log_returns, draws=250, tune=5000)

    # Interpret results
    results = interpret_changepoint(trace, dates, events_df)

    # Prepare output (use original daily data for prices)
    output = {
        "prices": price_df[["Date", "Price", "Log_Returns"]].to_dict(orient="records"),
        "change_point": results,
    }

    # Save to JSON
    output_path = Path("../dashboard/backend/data.json")
    output_path.parent.mkdir(parents=True, exist_ok=True)
    with open(output_path, "w") as f:
        json.dump(output, f, default=str)

    print(f"Dashboard data saved to: {output_path}")


if __name__ == "__main__":
    generate_dashboard_data()
