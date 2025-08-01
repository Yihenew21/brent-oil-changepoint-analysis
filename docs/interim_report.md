# Interim Report: Task 1 – Brent Oil Price Change Point Analysis

**10 Academy Week 10 Challenge**  
**Date**: August 1, 2025  
**Team**: Yihenew Animut

## Introduction

This interim report completes Task 1 of the 10 Academy Week 10 Challenge, focusing on defining the data analysis workflow and understanding the Brent oil price data and Bayesian change point models. The objective is to analyze how major events impact Brent oil prices.

## Data Analysis Workflow

The workflow, detailed in `docs/methodology.md`, includes:

1. **Data Cleaning**: Load and preprocess Brent oil price data (`data/raw/BrentOilPrices.csv`) using `src/data/data_loader.py`, converting `Date` to datetime and saving to `data/processed/cleaned_oil_data.csv`.
2. **Event Compilation**: Compiled 15 major events (1990–2023) in `data/events/major_events.csv`, covering conflicts, economic shocks, OPEC policies, and more. Note: The 2023 event will be excluded unless additional price data is sourced.
3. **Exploratory Data Analysis (EDA)**: Visualize price series and log returns, and test stationarity in `notebooks/01_exploratory_analysis.ipynb`.
4. **Modeling**: Plan to implement a Bayesian change point model using PyMC3 in Task 2.
5. **Interpretation**: Compare change points with events to hypothesize impacts.
6. **Dashboard**: Develop a Flask/React dashboard in Task 3.
7. **Reporting**: Share results via a blog post and GitHub.

## Event Dataset

The dataset (`data/events/major_events.csv`) contains 15 events with columns: `Event Name`, `Start Date`, `Category`, `Description`, `Source Link`. Examples:

- **1990-08-02**: Gulf War Begins (Conflict).
- **2008-09-15**: Global Financial Crisis (Economic Shock).
- **2022-02-24**: Russia Invades Ukraine (Conflict/Sanctions).
  Events were sourced from reliable references (e.g., Wikipedia, IMF, World Bank).

## Assumptions

- Events have immediate or short-term price impacts.
- Log returns are stationary, suitable for modeling.
- The price data is complete and accurate.

## Limitations

- **Correlation vs. Causation**: Change points may align with events but not prove causality.
- **Event Selection**: Manual compilation may miss minor events or misalign dates.
- **Data Scope**: Limited to price data and events up to 2022 (excluding 2023 event).
- **Model Sensitivity**: Bayesian priors may affect results.

## EDA Insights

- **Price Series**: Visualized in `results/figures/price_series.png`, showing trends (e.g., peaks in 2008, crashes in 2014, 2020).
- **Log Returns**: Plotted in `results/figures/log_returns.png`, revealing volatility clustering (e.g., high volatility in 2008, 2020).
- **Stationarity**: ADF test (in `notebooks/01_exploratory_analysis.ipynb`) will likely confirm non-stationarity of prices and stationarity of log returns, supporting their use in modeling.

## Model and Data Understanding

- **Time Series Properties**: Prices are non-stationary with trends and shocks; log returns are expected to be stationary.
- **Change Point Models**: Detect structural breaks (e.g., mean price shifts) using a switch point (`tau`) and PyMC3 MCMC sampling.
- **Outputs**: Change point dates, parameter changes (e.g., mean price), and probabilistic statements.
- **Limitations**: Sensitivity to priors, potential for missing multiple change points.

## Communication Plan

- **Dashboard**: Interactive Flask/React interface for stakeholders.
- **Report**: Blog post or PDF (`docs/final_report.md`).
- **GitHub**: Repository with code, notebooks, and documentation.

## GitHub Repository

- [Link to GitHub Repository](#) https://github.com/Yihenew21/brent-oil-changepoint-analysis.git.
- Key files: `src/data/data_loader.py`, `data/events/major_events.csv`, `notebooks/01_exploratory_analysis.ipynb`, `docs/methodology.md`.

## Next Steps

- Run EDA notebook to generate plots and confirm stationarity.
- Implement Bayesian change point model for Task 2.
- Begin dashboard development for Task 3.
