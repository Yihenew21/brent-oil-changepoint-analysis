import pandas as pd
from pathlib import Path

def load_brent_oil_data(raw_path: str, processed_path: str) -> pd.DataFrame:
    """
    Load and preprocess Brent oil price data, saving cleaned data to processed path.

    Args:
        raw_path (str): Path to raw Brent oil price CSV file.
        processed_path (str): Path to save processed CSV file.

    Returns:
        pd.DataFrame: Cleaned DataFrame with 'Date' as datetime and 'Price' as float.

    Raises:
        FileNotFoundError: If raw_path does not exist.
        ValueError: If required columns are missing or data is invalid.
    """
    # Check if raw file exists
    if not Path(raw_path).exists():
        raise FileNotFoundError(f"Raw data file not found at {raw_path}")

    # Load raw data
    df = pd.read_csv(raw_path)

    # Validate required columns
    required_cols = ['Date', 'Price']
    if not all(col in df.columns for col in required_cols):
        raise ValueError(f"Missing required columns: {required_cols}")

    # Convert Date to datetime - handle multiple formats
    def parse_dates(date_series):
      """Parse dates with multiple formats"""
      for fmt in ['%d-%b-%y', '%b %d, %Y', '%Y-%m-%d']:
          try:
             return pd.to_datetime(date_series, format=fmt)
          except ValueError:
            continue
      # If all formats fail, try pandas automatic parsing
      return pd.to_datetime(date_series)

    df['Date'] = parse_dates(df['Date'])

    # Ensure Price is numeric, handle missing values
    df['Price'] = pd.to_numeric(df['Price'], errors='coerce')
    if df['Price'].isna().sum() > 0:
        # Fill missing prices with forward fill
        df['Price'].fillna(method='ffill', inplace=True)

    # Sort by Date
    df = df.sort_values('Date').reset_index(drop=True)

    # Save cleaned data
    Path(processed_path).parent.mkdir(parents=True, exist_ok=True)
    df.to_csv(processed_path, index=False)

    return df