# Brent Oil Price Change Point Analysis

## Overview

This repository contains the implementation for the **10 Academy Artificial Intelligence Mastery Week 10 Challenge** (July 30 – August 5, 2025). The project analyzes the impact of major geopolitical, economic, and OPEC-related events on Brent oil prices using Bayesian change point modeling. The goal is to provide actionable insights for investors, policymakers, and energy companies at **Birhan Energies**, a consultancy specializing in energy market intelligence.

### Objectives

- **Task 1**: Define the data analysis workflow, compile an event dataset, and understand the Brent oil price data and change point models.
- **Task 2**: Implement a Bayesian change point model using PyMC3 to detect structural breaks in Brent oil prices and associate them with events.
- **Task 3**: Develop an interactive Flask/React dashboard to visualize results.

### Data

- **Brent Oil Prices**: Daily prices from May 20, 1987, to September 30, 2022 (`data/raw/BrentOilPrices.csv`).
- **Event Dataset**: 15 major events (1990–2022) compiled in `data/events/major_events.csv`, covering conflicts, economic shocks, and OPEC policies.

## 🚀 Quick Start Guide

### Prerequisites Checklist
Before starting, verify you have:
- [ ] Python 3.9+ installed (`python --version`)
- [ ] Node.js installed (`node --version`)
- [ ] Git installed (`git --version`)

### Step-by-Step Setup

#### 1. Clone and Navigate to Repository
```bash
git clone https://github.com/Yihenew21/brent-oil-changepoint-analysis.git
cd brent-oil-changepoint-analysis
```

#### 2. Set up Python Environment
Choose one option:

**Option A: Using venv (Recommended)**
```bash
python -m venv venv
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate
pip install -r requirements.txt
```

**Option B: Using Conda**
```bash
conda env create -f environment.yml
conda activate brent-oil-analysis
```

**Verification**: Run `pip list` - you should see packages like `pandas`, `pymc3`, `flask` installed.

#### 3. Install Frontend Dependencies
```bash
cd dashboard/frontend
npm install
cd ../..
```

**Verification**: Check that `node_modules` folder exists in `dashboard/frontend/`

#### 4. Data Setup
```bash
# Ensure data files are in place
ls data/raw/BrentOilPrices.csv     # Should exist
ls data/events/major_events.csv    # Should exist (included)
```

**Important**: If `BrentOilPrices.csv` is missing, place your Brent oil price data file in the `data/raw/` directory.

## 📋 Complete Analysis Workflow

### Task 1: Data Analysis Workflow and Event Dataset

#### Run Exploratory Data Analysis
```bash
# Launch Jupyter notebook
jupyter notebook notebooks/01_exploratory_analysis.ipynb
```

**Expected Output**: 
- Visualization of price series showing trends (peaks in 2008, crashes in 2014, 2020)
- Log returns plot revealing volatility clustering
- Stationarity test results (ADF test)
- Plots saved to `results/figures/price_series.png` and `results/figures/log_returns.png`

#### View Event Dataset
The major events dataset includes 15 events such as:
- **1990-08-02**: Gulf War Begins (Conflict)
- **2008-09-15**: Global Financial Crisis (Economic Shock)  
- **2022-02-24**: Russia Invades Ukraine (Conflict/Sanctions)

### Task 2: Bayesian Change Point Modeling

#### Step 1: Data Preprocessing
```bash
jupyter notebook notebooks/02_data_preprocessing.ipynb
```

**What this does**:
- Converts Date column to datetime format
- Computes log returns: `log(price_t) - log(price_{t-1})`
- Saves cleaned data to `data/processed/cleaned_oil_data.csv`

**Verification**: Check that `data/processed/cleaned_oil_data.csv` is created.

#### Step 2: Run Change Point Modeling
```bash
jupyter notebook notebooks/03_changepoint_modeling.ipynb
```

**What this does**:
- Implements Bayesian change point model using PyMC3
- Defines switch point (`tau`) as DiscreteUniform prior
- Specifies Normal priors for mean log returns before (`mu_1`) and after (`mu_2`) the switch point
- Runs MCMC sampling (1000 draws, 1000 tuning samples)
- Associates detected change points with closest events (within 30 days)

**Expected Output**:
- Model convergence with `r_hat` values close to 1.0
- Change point detection (e.g., around 2008 aligning with Global Financial Crisis)
- Impact quantification (change in mean log returns)
- Visualization saved to `results/figures/changepoint_results.png`

#### Step 3: Results Interpretation
```bash
jupyter notebook notebooks/04_results_interpretation.ipynb
```

**What you'll see**:
- Change point dates from posterior distribution of `tau`
- Associated events matched to change points
- Quantified price impacts (percentage changes in mean price)

### Task 3: Interactive Dashboard

#### Step 1: Run Main Analysis Script
```bash
python scripts/run_analysis.py
```

#### Step 2: Generate Dashboard Data
```bash
python scripts/generate_dashboard_data.py
```

#### Step 3: Launch Dashboard

**Terminal 1 - Start Backend:**
```bash
cd dashboard/backend
python app.py
```
**Expected Output**: `Running on http://127.0.0.1:5000`

**Terminal 2 - Start Frontend:**
```bash
cd dashboard/frontend
npm start
```
**Expected Output**: `Local: http://localhost:3000`

**Final Step**: Open your browser to `http://localhost:3000` to view the interactive dashboard.

## 📁 Repository Structure

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
│   │   └── BrentOilPrices.csv      # Main dataset (user provided)
│   ├── processed/          # Cleaned data (generated by notebooks)
│   │   └── cleaned_oil_data.csv    # Preprocessed data
│   └── events/             # Event dataset
│       └── major_events.csv       # 15 major events (1990-2022)
│
├── notebooks/
│   ├── 01_exploratory_analysis.ipynb  # EDA for price series
│   ├── 02_data_preprocessing.ipynb    # Data cleaning and log returns
│   ├── 03_changepoint_modeling.ipynb  # Bayesian modeling with PyMC3
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
│   │   └── app.py          # Main Flask application
│   └── frontend/           # React frontend
│       ├── src/            # React components
│       ├── package.json    # Node.js dependencies
│       └── node_modules/   # Installed packages (after npm install)
│
├── results/
│   ├── figures/            # Generated plots
│   │   ├── price_series.png        # Oil price visualization
│   │   ├── log_returns.png         # Log returns plot
│   │   └── changepoint_results.png # Change point analysis
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
│   ├── methodology.md      # Detailed methodology
│   └── task_2_report.md    # Task 2 completion report
│
└── scripts/
    ├── run_analysis.py     # Main analysis script
    └── generate_dashboard_data.py  # Dashboard data preparation
```

## 🔍 Expected Results and Outputs

### After Task 1 (EDA):
- **Files Created**: 
  - `results/figures/price_series.png` - Shows price trends with peaks and crashes
  - `results/figures/log_returns.png` - Displays volatility clustering
- **Key Insights**: Price series non-stationary, log returns stationary, volatility clustering evident

### After Task 2 (Modeling):
- **Files Created**:
  - `data/processed/cleaned_oil_data.csv` - Preprocessed data with log returns
  - `results/figures/changepoint_results.png` - Change point visualization
  - Model artifacts in `results/models/`
- **Key Results**: 
  - Detected change points (e.g., around 2008 Global Financial Crisis)
  - Quantified impact (change in mean log returns)
  - Event associations within 30-day windows

### After Task 3 (Dashboard):
- **Dashboard Features** at `http://localhost:3000`:
  - Interactive oil price charts
  - Change point detection visualization  
  - Event correlation timeline
  - Results from Bayesian analysis

## 🛠️ Troubleshooting Common Issues

### Issue: "ModuleNotFoundError: No module named 'pymc3'"
**Solution**:
```bash
pip install --upgrade pip
pip install -r requirements.txt
```

### Issue: "FileNotFoundError: data/raw/BrentOilPrices.csv"
**Solution**: Ensure you have placed the Brent oil price data file in the `data/raw/` directory. The file should contain daily prices from May 20, 1987, to September 30, 2022.

### Issue: Dashboard connection errors
**Solution**:
```bash
# Check if both services are running
# Backend should show: "Running on http://127.0.0.1:5000"
# Frontend should show: "Local: http://localhost:3000"

# If ports are busy, find and kill processes:
# On Windows: netstat -ano | findstr :3000
# On macOS/Linux: lsof -i :3000
```

### Issue: Jupyter notebooks not opening
**Solution**:
```bash
# Ensure Jupyter is installed
pip install jupyter

# Launch from project root directory
jupyter notebook
```

## 📊 Key Dependencies

### Python Packages (requirements.txt):
```
pandas>=1.5.0       # Data manipulation and analysis
numpy>=1.21.0       # Numerical computing
matplotlib>=3.5.0   # Data visualization
statsmodels>=0.13.0 # Statistical modeling and tests
pymc3>=3.11.0       # Bayesian modeling and MCMC
flask>=2.0.0        # Web framework for backend
jupyter>=1.0.0      # Interactive notebook environment
```

### Node.js Packages (dashboard/frontend/package.json):
- React for frontend interface
- Plotting libraries for interactive visualizations
- HTTP client for API communication

## 📈 Model Understanding

### Bayesian Change Point Model Details:
- **Switch Point (`tau`)**: DiscreteUniform prior over all time points
- **Mean Parameters**: 
  - `mu_1`: Mean log returns before change point (Normal prior, centered at 0)
  - `mu_2`: Mean log returns after change point (Normal prior, centered at 0)
- **Standard Deviation**: `sigma` with HalfNormal prior
- **Likelihood**: Normal distribution with switching mean based on `tau`
- **Sampling**: MCMC with 1000 draws and 1000 tuning samples

### Model Assumptions:
- Single change point captures major structural breaks
- Log returns follow Normal distribution around the mean
- Events within 30 days of change points are potential causes

### Model Limitations:
- May miss multiple change points (addressed in future work)
- Assumes correlation implies causation for event association
- Focuses on mean shifts, not volatility changes

## 🤝 Contributing

- Create a feature branch: `git checkout -b feature/your-feature`
- Commit changes: `git commit -m "Add your feature"`
- Push and create a pull request: `git push origin feature/your-feature`

## 📄 License

MIT License (see `LICENSE` file, to be added).

## 📞 Contact

For questions, contact YIHENEW or post issues on the GitHub repository: https://github.com/Yihenew21/brent-oil-changepoint-analysis

---

**Project Status**: ✅ Task 1 | 🔄Task 2 partial Complete | 🔄  Task 3 In Progress  
**Last Updated**: August 2025