
import requests
from datetime import datetime, timezone
from .config import API_KEY_POLYGON


BASE_URL = "https://api.polygon.io"

def get_stock_data(tickers: list[str], start_date: str, end_date: str):
    """
    Query historical stock closing data using Polygon.io

    Args:
        tickers (list): List of stock symbols (e.g., ["AAPL", "TSLA"]).
        start_date (str): Start date in YYYY-MM-DD format.
        end_date (str): End date in YYYY-MM-DD format.

    Returns:
        dict: Dictionary of daily closing data per stock
    """
    data = {}

    for ticker in tickers:
        url = f"{BASE_URL}/v2/aggs/ticker/{ticker}/range/1/day/{start_date}/{end_date}?adjusted=true&sort=asc&apiKey={API_KEY_POLYGON}"
        
        response = requests.get(url)
        if response.status_code != 200:
            print(f"[ERROR] No data could be obtained for {ticker}")
            data[ticker] = {"error": response.json()}
            continue

        results = response.json().get("results", [])
        data[ticker] = [
            {
                "date": datetime.fromtimestamp(day["t"] / 1000, tz=timezone.utc).strftime("%Y-%m-%d"),
                "close": day["c"]
            }
            for day in results
        ]

    return data