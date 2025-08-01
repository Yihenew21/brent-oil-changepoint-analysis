# Interim Report: Task 1 – Brent Oil Price Change Point Analysis

**10 Academy Week 10 Challenge**  
**Date**: August 1, 2025  
**Team**: [Your Name/Team Name]

## Introduction

This interim report outlines the planned data analysis workflow, event dataset compilation, and initial steps for Task 1 of the 10 Academy Week 10 Challenge. The goal is to analyze how major events impact Brent oil prices using Bayesian change point modeling.

## Planned Steps

1. **Data Cleaning**:

   - Load Brent oil price data (`data/raw/brent_oil_prices.csv`) using `src/data/data_loader.py`.
   - Convert `Date` to datetime and ensure `Price` is numeric.
   - Save cleaned data to `data/processed/cleaned_oil_data.csv`.

2. **Event Compilation**:

   - Researched 11 major events (e.g., 2008 financial crisis, 2020 OPEC+ price war) and compiled them in `data/events/major_events.csv`.
   - Events include geopolitical conflicts, OPEC policies, and demand/supply shocks.

3. **Exploratory Data Analysis**:

   - Visualize price series and log returns in `notebooks/01_exploratory_analysis.ipynb`.
   - Test stationarity using the Augmented Dickey-Fuller test to confirm log returns are suitable for modeling.

4. **Model Development**:

   - Implement a Bayesian change point model in `src/models/changepoint_model.py` using PyMC3.
   - Define a switch point (`tau`) and estimate parameter changes (e.g., mean price).

5. **Interpretation**:

   - Compare change points with events to hypothesize causal relationships.
   - Quantify price impacts (e.g., percentage changes).

6. **Dashboard**:

   - Develop a Flask/React dashboard to visualize results interactively.

7. **Reporting**:
   - Submit a final report or blog post and share via GitHub.

## Event Dataset

The event dataset (`data/events/major_events.csv`) includes 11 events with columns: `Date`, `Event`, `Description`, `Category`. Examples:

- **01-Jan-2008**: Global Financial Crisis (Oil Demand Shock).
- **01-Nov-2016**: OPEC Production Cut (OPEC Policy).
- **01-Jan-2022**: Russia-Ukraine Conflict (Geopolitical Conflict).

## Assumptions and Limitations

- **Assumptions**: Events have immediate impacts; log returns are stationary.
- **Limitations**: Correlation does not imply causation; event selection may introduce bias.

## GitHub Repository

- [Link to GitHub Repository](#) (to be updated with actual link).
- Code includes `src/data/data_loader.py`, `notebooks/01_exploratory_analysis.ipynb`, and `data/events/major_events.csv`.

## Next Steps

- Complete EDA and confirm stationarity.
- Implement the Bayesian model for Task 2.
- Begin dashboard development for Task 3.
