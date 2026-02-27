from __future__ import annotations

import pandas as pd
import yfinance as yf


def fetch_close_prices(symbol: str, start: str, end: str) -> pd.Series:
    """Download adjusted close prices for a symbol and date range."""
    data = yf.download(symbol, start=start, end=end, auto_adjust=True, progress=False)
    if data.empty:
        raise ValueError(f"No data returned for {symbol} between {start} and {end}.")

    close = data["Close"].rename("close")
    close.index = pd.to_datetime(close.index)
    return close
