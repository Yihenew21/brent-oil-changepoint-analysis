# Task 2 Report: Change Point Modeling and Insight Generation

**10 Academy Week 10 Challenge**  
**Date**: August 5, 2025  
**Team**: [Your Name/Team Name]

## Introduction
This report completes Task 2 (Part 2.1) of the 10 Academy Week 10 Challenge, implementing a Bayesian change point model using PyMC to detect structural breaks in Brent oil price log returns, identifying change points, associating them with events, and quantifying impacts.

## Methodology
1. **Data Preparation**:
   - Preprocessed Brent oil price data in `notebooks/02_data_preprocessing.ipynb`, computing log returns and saving to `data/processed/cleaned_oil_data.csv`.
   - Loaded preprocessed data (9,010 days, log returns from -0.6437 to 0.4120) and events (`data/events/major_events.csv`) in `notebooks/03_changepoint_modeling.ipynb`.
   - Downsampled to weekly data (~1,300 weeks) to improve model efficiency.
   - Used log returns for modeling due to stationarity (confirmed in `notebooks/01_exploratory_analysis.ipynb`).

2. **Model Implementation**:
   - Built a Bayesian change point model in `src/models/changepoint_model.py` using PyMC.
   - Defined a switch point (`tau`) as a categorical prior (every 20th week, ~65 possibilities).
   - Specified `Normal` priors for mean log returns before (`mu_1`) and after (`mu_2`), centered at 0.
   - Used a `HalfNormal` prior for standard deviation (`sigma`).
   - Applied a `Normal` likelihood with a switch function.
   - Ran MCMC sampling (250 draws, 5,000 tuning samples, 4 chains) with a hybrid `Metropolis`/`NUTS` sampler and data-informed initialization.

3. **Results Interpretation**:
   - Plotted log returns with the mean change point and posterior distribution of `tau` (pending confirmation in `results/figures/changepoint_results.png`).
   - Identified the change point date from the mean of `tau`’s posterior.
   - Associated the change point with the closest event in `major_events.csv` (within 30 days).
   - Quantified the impact by comparing mean log returns before and after (`mu_1` vs. `mu_2`).

## Results
- **Data Summary**: 9,010 daily observations, downsampled to ~1,300 weekly observations, log returns ranging from -0.6437 to 0.4120 (adjusted).
- **Model Convergence**: Run (5,000 tuning) took 4794 seconds with 229 divergences, `r_hat` > 1.01 (e.g., `tau_idx`: 1.3428, `mu_2`: 1.5439), and low `ess_bulk` (e.g., `tau_idx`: 9.9592, `mu_2`: 7.2100), indicating sampling issues.
- **Change Point**: 2006-05-14, detected ~2.3 years before the Lehman collapse.
- **Associated Event**: Global Financial Crisis (event date: 2008-09-15).
- **Visualization**: Plot saved to `results/figures/changepoint_results.png` (pending upload).
- **Log Return Change**: -0.0003, from `mu_1` (0.0002) to `mu_2` (-0.0002).

## Assumptions
- A single change point captures major shifts in log return behavior.
- Log returns follow a `Normal` distribution around the mean before/after the change point.
- Weekly downsampling preserves major structural breaks.
- The closest event within 30 days is the likely cause of the change point.

## Limitations
- **Single Change Point**: May miss multiple breaks (e.g., 2008 peak, 2020 crash).
- **Downsampling**: Weekly data smooths short-term price movements, reducing impact magnitude.
- **Convergence**: 229 divergences and high `r_hat` values suggest unreliable parameter estimates; increasing `target_accept` or reparameterization is needed.
- **Impact Magnitude**: The -0.0003 log return change is negligible compared to the GFC’s ~$147 to ~$30/barrel drop, likely due to model limitations.
- **Causation**: Associating 2006-05-14 with the 2008 GFC assumes early market signals, but the 2.3-year gap weakens this link.

## Future Work (Part 2.2)
- **Multiple Change Points**: Use a Dirichlet process to detect breaks for all major events (e.g., 2008, 2020).
- **Advanced Models**: Explore VAR or Markov-Switching models to capture dynamic relationships and market regimes.
- **Additional Data**: Incorporate macroeconomic variables (e.g., GDP, inflation) for a comprehensive model.

## GitHub Repository
- [Link to GitHub Repository](#) (to be updated).
- Key files: `notebooks/02_data_preprocessing.ipynb`, `src/models/changepoint_model.py`, `notebooks/03_changepoint_modeling.ipynb`, `results/figures/changepoint_results.png`.

## Next Steps
- Complete Task 3 (Flask/React dashboard).
- Prepare `docs/final_report.md` by August 5, 2025.