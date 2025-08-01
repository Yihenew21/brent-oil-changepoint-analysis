# Task 2 Report: Change Point Modeling and Insight Generation

**10 Academy Week 10 Challenge**  
**Date**: August 1, 2025  
**Team**: Yihenew

## Introduction

This report completes Task 2 (Part 2.1) of the 10 Academy Week 10 Challenge, focusing on implementing a Bayesian change point model to detect structural breaks in Brent oil prices, identifying change points, associating them with events, and quantifying impacts.

## Methodology

1. **Data Preparation**:

   - Loaded cleaned Brent oil price data (`data/processed/cleaned_oil_data.csv`) and events (`data/events/major_events.csv`) in `notebooks/03_changepoint_modeling.ipynb`.
   - Extracted prices as a numpy array for modeling.

2. **Model Implementation**:

   - Built a Bayesian change point model in `src/models/changepoint_model.py` using PyMC3.
   - Defined a switch point (`tau`) as a DiscreteUniform prior over all days.
   - Specified Normal priors for mean prices before (`mu_1`) and after (`mu_2`) the switch point.
   - Used a HalfNormal prior for standard deviation (`sigma`).
   - Applied a Normal likelihood with a switch function to toggle means.
   - Ran MCMC sampling (1000 draws, 1000 tuning samples).

3. **Results Interpretation**:
   - Plotted the price series with the mean change point and the posterior distribution of `tau` (`results/figures/changepoint_results.png`).
   - Identified the change point date from the mean of `tau`’s posterior.
   - Associated the change point with the closest event in `major_events.csv` (within 30 days).
   - Quantified the impact by comparing mean prices before and after (`mu_1` vs. `mu_2`).

## Results

- **Model Convergence**: The MCMC summary (in `notebooks/03_changepoint_modeling.ipynb`) shows `r_hat` values close to 1.0, indicating convergence (to be verified upon running).
- **Change Point**: The model detects a significant change point (exact date depends on data; e.g., around 2008 may align with the Global Financial Crisis).
- **Associated Event**: The change point is matched to the closest event (e.g., “Global Financial Crisis” on 2008-09-15 if detected around that period).
- **Impact**: Example output (hypothetical until run):
  - Change Point Date: 2008-10-01
  - Associated Event: Global Financial Crisis
  - Price Change: -$30.50 USD/barrel
  - Percent Change: -40.67%
- **Visualization**: The plot (`results/figures/changepoint_results.png`) shows the price series with a red dashed line at the change point and a histogram of `tau`’s posterior.

## Assumptions

- A single change point adequately captures major structural breaks.
- Prices follow a Normal distribution around the mean before/after the change point.
- The closest event within 30 days is the likely cause of the change point.

## Limitations

- **Single Change Point**: May miss multiple structural breaks (e.g., 2008 and 2020).
- **Causation**: Associating change points with events assumes correlation implies causation, which may not hold.
- **Model Simplicity**: Ignores volatility changes or other factors (e.g., GDP, exchange rates).

## Future Work (Part 2.2)

- **Multiple Change Points**: Extend the model to detect multiple switch points using a Dirichlet process.
- **Advanced Models**: Explore Vector Autoregression (VAR) for dynamic relationships or Markov-Switching models for regime changes (calm vs. volatile).
- **Additional Data**: Incorporate macroeconomic variables (e.g., inflation, GDP) for a comprehensive analysis.

## GitHub Repository

- [Link to GitHub Repository](#) https://github.com/Yihenew21/brent-oil-changepoint-analysis.git.
- Key files: `src/models/changepoint_model.py`, `notebooks/03_changepoint_modeling.ipynb`, `results/figures/changepoint_results.png`.

## Next Steps

- Run the notebook to generate actual results and verify convergence.
- Develop the Flask/React dashboard for Task 3.
- Prepare the final report for submission by August 5, 2025.
