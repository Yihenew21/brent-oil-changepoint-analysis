"""Flask backend to serve data for the Brent oil price dashboard."""

from flask import Flask, jsonify
import json
from pathlib import Path
from flask_cors import CORS

app = Flask(__name__)
CORS(
    app, resources={r"/api/*": {"origins": "http://localhost:5173"}}
)  # Enable CORS for API routes

# Load data from JSON file with relative path
data_path = Path("data.json")
if not data_path.exists():
    raise FileNotFoundError(
        "data.json not found. Ensure generate_dashboard_data.py ran successfully."
    )
with open(data_path, "r") as f:
    dashboard_data = json.load(f)


@app.route("/")
def home():
    """Redirect to API documentation or a simple message."""
    return "Brent Oil Price Dashboard API. Use /api/prices or /api/change-point."


@app.route("/api/prices", methods=["GET"])
def get_prices():
    """Return price data including dates, prices, and log returns."""
    return jsonify(dashboard_data["prices"])


@app.route("/api/change-point", methods=["GET"])
def get_change_point():
    """Return change point analysis results."""
    return jsonify(dashboard_data["change_point"])


if __name__ == "__main__":
    app.run(debug=True, port=5000)
