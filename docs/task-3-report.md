# Task 3 Report: Brent Oil Price Analysis Dashboard

## Overview
This report documents the development and testing of the Brent Oil Price Analysis Dashboard, a web-based application designed to visualize historical Brent oil price trends and identify significant change points. The dashboard leverages React for the frontend, Chart.js for data visualization, and a Flask backend to serve data from a JSON file (`data.json`). The project was completed with a focus on resolving data fetching, filtering, and rendering issues encountered during development.

## Objectives
- Develop a dashboard to display log returns of Brent oil prices over time.
- Implement an interactive date filter to isolate specific days.
- Highlight significant change points (e.g., the Arab Spring event on 2010-09-05).
- Ensure robust data handling and error resolution.

## Implementation

### Backend
- **Technology**: Flask
- **File**: `app.py`
- **Functionality**: 
  - Serves price data and change point analysis via `/api/prices` and `/api/change-point` endpoints.
  - Loads data from `data.json` using relative path handling with `pathlib.Path`.
  - Configured with `flask-cors` to enable cross-origin requests from the frontend (`http://localhost:5173`).
- **Challenges**: Initial CORS issues blocked data fetching, resolved by adding CORS support.

### Frontend
- **Technology**: React, Vite, Chart.js
- **File**: `App.jsx`
- **Functionality**:
  - Fetches and displays price data as a line chart of log returns.
  - Implements a date filter using an `<input type="date">` to subset data.
  - Highlights change points with larger point radii on the chart.
  - Displays change point details (date, event, log return change, etc.) below the chart.
- **Challenges**:
  - Initial CORS errors prevented data loading, fixed with backend update.
  - `TypeError: prices.filter is not a function` due to data structure mismatch, resolved by ensuring `prices` is an array.
  - Chart not rendering due to missing `Filler` plugin, addressed by registering it.
  - Filtering issues due to date format mismatches, handled by extracting date parts with `.split(' ')[0]`.

## Data
- **Source**: `data.json`
- **Content**: Historical Brent oil prices with dates, prices, and log returns, plus a change point object.
- **Sample**: 
  - First entry: `"Date": "1987-05-20 00:00:00", "Log_Returns": NaN, "Price": 18.63`
  - Change point: `"change_point_date": "2010-09-05", "associated_event": "Arab Spring"`
- **Notes**: Data includes `NaN` values (e.g., first log return), filtered out in the chart.

## Testing and Results
- **Environment**: Localhost (Flask on port 5000, Vite on port 5173)
- **Tests Performed**:
  - Verified data fetching via console logs (`Prices data:` and `Change point data:`).
  - Tested date filter with valid dates (e.g., `1987-05-21`), expecting single-point graphs.
  - Checked change point highlighting for `2010-09-05`.
- **Outcomes**:
  - CORS issues resolved, enabling data access.
  - Graph renders log returns after fixing data structure and plugin issues.
  - Date filtering works for dates present in data (e.g., `1987-05-21`).
  - Change point details display correctly, though full dataset beyond July 1987 requires testing.

## Limitations and Future Work
- **Limitations**: 
  - Current data is truncated (up to July 1987), limiting change point visibility (e.g., 2010-09-05 not in sample).
  - No error boundaries implemented for robust user experience.
- **Future Work**:
  - Integrate full dataset to verify 2010-09-05 change point.
  - Add error boundaries and loading states.
  - Enhance UI with additional metrics (e.g., moving averages).

## Conclusion
The Brent Oil Price Analysis Dashboard successfully visualizes log returns and supports interactive filtering. Key issues (CORS, data structure, plugin registration) were resolved, enabling a functional prototype. With the full dataset and further refinements, the dashboard will meet all project objectives.

## Submission Details
- **Date**: August 5, 2025
- **Time**: 06:57 AM EAT (~03:57 UTC)
