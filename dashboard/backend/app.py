"""Flask backend to serve data for the Brent oil price dashboard."""
from flask import Flask, jsonify
import json
from pathlib import Path

app = Flask(__name__)

# Load data from JSON file
data_path = Path('data.json')
if not data_path.exists():
    raise FileNotFoundError("data.json not found. Run generate_dashboard_data.py first.")
with open(data_path, 'r') as f:
    dashboard_data = json.load(f)

@app.route('/api/prices', methods=['GET'])
"""Return price data including dates, prices, and log returns."""
def get_prices():
    return jsonify(dashboard_data['prices'])

@app.route('/api/change-point', methods=['GET'])
"""Return change point analysis results."""
def get_change_point():
    return jsonify(dashboard_data['change_point'])

if __name__ == '__main__':
    app.run(debug=True, port=5000)