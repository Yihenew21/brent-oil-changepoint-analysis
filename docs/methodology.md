# Data Analysis Workflow for Brent Oil Price Change Point Analysis

## Overview

This document outlines the data analysis workflow for analyzing the impact of major events on Brent oil prices using Bayesian change point modeling. It includes steps, assumptions, limitations, communication strategies, and model/data understanding as part of Task 1 for the 10 Academy Week 10 Challenge.

## Analysis Steps

1. **Data Collection and Cleaning**:

   - Load Brent oil price data (`brent_oil_prices.csv`) from May 20, 1987, to September 30, 2022.
   - Convert `Date` column to datetime format and ensure `Price` is numeric.
   - Handle missing values or outliers, if any.
   - Save cleaned data to `data/processed/cleaned_oil_data.csv`.

2. **Event Data Compilation**:

   - Research 10–15 major geopolitical, economic, and OPEC-related events (e.g., conflicts, sanctions, policy changes).
   - Create a structured dataset (`data/events/major_events.csv`) with columns: `Date`, `Event`, `Description`, `Category`.
   - Cross-reference events with reliable sources (e.g., OPEC reports, news archives).

3. **Exploratory Data Analysis (EDA)**:

   - Visualize raw price series to identify trends, shocks, and volatility.
   - Compute log returns (`log(price_t) - log(price_{t-1})`) to analyze stationarity and volatility clustering.
   - Perform stationarity tests (e.g., Augmented Dickey-Fuller) to inform modeling choices.
   - Save plots to `results/figures/`.

4. **Bayesian Change Point Modeling**:

   - Implement a Bayesian change point model using PyMC3 in `src/models/changepoint_model.py`.
   - Define a switch point (`tau`) and parameters (e.g., mean prices before/after).
   - Run MCMC sampling to estimate posterior distributions.
   - Save model outputs to `results/models/`.

5. **Change Point Interpretation**:

   - Identify significant change points from the posterior distribution of `tau`.
   - Compare change point dates with events in `major_events.csv` to hypothesize causal relationships.
   - Quantify price impacts (e.g., percentage changes in mean price).

6. **Dashboard Development**:

   - Build a Flask backend (`dashboard/backend/app.py`) to serve analysis results via APIs.
   - Develop a React frontend (`dashboard/frontend/src/`) with interactive visualizations (e.g., price trends, event highlights).
   - Deploy the dashboard for stakeholder access.

7. **Reporting and Communication**:
   - Write an interim report (`docs/interim_report.md`) for Task 1.
   - Prepare a final report or blog post (`docs/final_report.md`) summarizing findings.
   - Share results via a Medium blog post and GitHub repository.

## Assumptions

- **Event Impact**: Major events (e.g., OPEC decisions, conflicts) have immediate or short-term impacts on Brent oil prices.
- **Data Quality**: The provided price data is complete and accurate, with minimal missing values.
- **Model Simplicity**: A single or few switch points adequately capture structural breaks in the price series.
- **Stationarity**: Log returns of prices are stationary, suitable for modeling volatility changes.

## Limitations

- **Correlation vs. Causation**: Detected change points may correlate with events but not prove causation due to unmodeled factors (e.g., weather, technology).
- **Event Selection Bias**: Manually compiled events may miss minor but impactful events or misalign dates.
- **Model Sensitivity**: Bayesian models depend on prior assumptions, which may affect change point detection.
- **Data Scope**: The analysis is limited to price data and compiled events, excluding other factors (e.g., GDP, exchange rates).

## Communication Channels

- **Primary**: Interactive dashboard (Flask/React) for stakeholders to explore price trends and event impacts.
- **Secondary**: PDF report or Medium blog post (`docs/final_report.md`) for detailed insights.
- **Technical**: GitHub repository with code, notebooks, and documentation for transparency.
- **Audience**: Investors, policymakers, and energy companies requiring actionable insights.

## Understanding the Model and Data

### Time Series Properties

- **Trend**: Brent oil prices exhibit long-term trends (e.g., rising from 1987–2008, crashing in 2008, recovering, then crashing again in 2014 and 2020). Visual inspection in `notebooks/01_exploratory_analysis.ipynb` confirms non-linear trends.
- **Stationarity**: The raw price series is likely non-stationary due to trends and volatility clustering. The Augmented Dickey-Fuller (ADF) test will confirm this. Log returns (`log(price_t) - log(price_{t-1})`) are expected to be stationary, making them suitable for modeling volatility changes.
- **Volatility Clustering**: Periods of high volatility (e.g., 2008 crisis, 2020 pandemic) are followed by more volatility, observable in log returns plots.

### Change Point Models

- **Purpose**: Bayesian change point models detect structural breaks in time series data, such as shifts in mean price or volatility. They are ideal for identifying when and how Brent oil price behavior changes due to external events.
- **Mechanism**: The model defines a switch point (`tau`) where parameters (e.g., mean price) change. Using PyMC3, we estimate the posterior distribution of `tau` and parameters via MCMC sampling.
- **Expected Outputs**:
  - **Change Point Dates**: Posterior distribution of `tau` indicates likely dates of structural breaks.
  - **Parameter Changes**: Differences in mean price or volatility before/after `tau` (e.g., mean price shifts from $50 to $70).
  - **Probabilistic Statements**: E.g., “95% probability the mean price increased after the change point.”
- **Limitations**:
  - **Prior Sensitivity**: Results depend on prior distributions for `tau` and parameters.
  - **Single Switch Point**: A simple model may miss multiple change points.
  - **Causation**: Change points may align with events but not confirm causality without further analysis.
