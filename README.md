# Brent Oil Price Change Point Analysis

## Overview

This repository contains the implementation for the **10 Academy Artificial Intelligence Mastery Week 10 Challenge** (July 30 – August 5, 2025). The project analyzes the impact of major geopolitical, economic, and OPEC-related events on Brent oil prices using Bayesian change point modeling. The goal is to provide actionable insights for investors, policymakers, and energy companies at **Birhan Energies**, a consultancy specializing in energy market intelligence.

### Objectives

- **Task 1**: Define the data analysis workflow, compile an event dataset, and understand the Brent oil price data and change point models.
- **Task 2**: Implement a Bayesian change point model using PyMC3 to detect structural breaks in Brent oil prices and associate them with events.
- **Task 3**: Develop an interactive Flask/React dashboard to visualize results.

### Data

- **Brent Oil Prices**: Daily prices from May 20, 1987, to September 30, 2022 (`data/raw/brent_oil_prices.csv`).
- **Event Dataset**: 15 major events (1990–2022) compiled in `data/events/major_events.csv`, covering conflicts, economic shocks, and OPEC policies.

## Repository Structure

```
brent-oil-changepoint-analysis/
│
├── README.md                # Project overview and setup instructions
├── requirements.txt         # Python dependencies
├── .gitignore              # Git ignore file
├── environment.yml         # Conda environment (optional)
│
├── data/
│   ├── raw/                # Raw Brent oil price data
│   ├── processed/          # Cleaned data
│   └── events/             # Event dataset (major_events.csv)
│
├── notebooks/
│   ├── 01_exploratory_analysis.ipynb  # EDA for price series
│   ├── 02_data_preprocessing.ipynb    # Data cleaning
│   ├── 03_changepoint_modeling.ipynb  # Bayesian modeling
│   └── 04_results_interpretation.ipynb # Results analysis
│
├── src/
│   ├── data/
│   │   └── data_loader.py  # Data loading utilities
│   ├── models/
│   │   └── changepoint_model.py  # PyMC3 model implementation
│   ├── visualization/
│   │   └── plots.py        # Plotting functions
│   └── utils/
│       └── helpers.py      # Helper functions
│
├── dashboard/
│   ├── backend/            # Flask backend
│   └── frontend/           # React frontend
│
├── results/
│   ├── figures/            # Generated plots
│   ├── models/             # Saved model artifacts
│   └── reports/            # Generated reports
│
├── tests/
│   ├── test_data_loader.py # Unit tests for data loader
│   └── test_models.py      # Unit tests for models
│
├── docs/
│   ├── interim_report.md   # Task 1 submission
│   ├── final_report.md     # Final report/blog post
│   └── methodology.md      # Detailed methodology
│
└── scripts/
    ├── run_analysis.py     # Main analysis script
    └── generate_dashboard_data.py  # Dashboard data preparation
```

## Setup Instructions

### Prerequisites

- Python 3.9+
- Node.js (for React frontend)
- Git
- Conda (optional, for environment management)

### Installation

1. **Clone the repository**:

   ```bash
   git clone https://github.com/Yihenew21/brent-oil-changepoint-analysis.git
   cd brent-oil-changepoint-analysis
   ```

2. **Set up Python environment**:

   - Using `venv`:
     ```bash
     python -m venv venv
     source venv/bin/activate  # On Windows: venv\Scripts\activate
     pip install -r requirements.txt
     ```
   - Or using Conda:
     ```bash
     conda env create -f environment.yml
     conda activate brent-oil-analysis
     ```

3. **Install frontend dependencies** (for Task 3):

   ```bash
   cd dashboard/frontend
   npm install
   ```

4. **Place data**:
   - Add `BrentOilPrices.csv` to `data/raw/`.
   - The `major_events.csv` is already included in `data/events/`.

### Running the Analysis

1. **Exploratory Data Analysis**:

   ```bash
   jupyter notebook notebooks/01_exploratory_analysis.ipynb
   ```

2. **Run main analysis** (Tasks 2–3):

   ```bash
   python scripts/run_analysis.py
   ```

3. **Launch dashboard** (Task 3):
   ```bash
   cd dashboard/backend
   python app.py
   cd ../frontend
   npm start
   ```

## Usage

- **Task 1**: Run `notebooks/01_exploratory_analysis.ipynb` to visualize price trends and log returns.
- **Task 2**: Implement Bayesian change point modeling in `notebooks/03_changepoint_modeling.ipynb` (in progress).
- **Task 3**: Access the dashboard at `http://localhost:3000` after starting the backend and frontend.

## Deliverables

- **Interim Submission** (August 1, 2025):
  - `docs/interim_report.md`
  - `data/events/major_events.csv`
  - GitHub repository link
- **Final Submission** (August 5, 2025):
  - `docs/final_report.md` (blog post or PDF)
  - GitHub repository with code and screenshots

## Dependencies

Key Python packages (`requirements.txt`):

```
pandas>=1.5.0
numpy>=1.21.0
matplotlib>=3.5.0
statsmodels>=0.13.0
pymc3>=3.11.0
```

## Contributing

- Create a feature branch: `git checkout -b feature/your-feature`
- Commit changes: `git commit -m "Add your feature"`
- Push and create a pull request: `git push origin feature/your-feature`

## License

MIT License (see `LICENSE` file, to be added).

## Contact

For questions, contact YIHENEW or post issues on the GitHub repository.
