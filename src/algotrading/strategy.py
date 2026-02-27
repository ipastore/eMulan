from __future__ import annotations

import pandas as pd


def sma_crossover_signals(
    prices: pd.Series, fast_window: int = 20, slow_window: int = 50
) -> pd.Series:
    """Return long-only signals (1 for long, 0 for cash) based on SMA crossover."""
    if fast_window <= 0 or slow_window <= 0:
        raise ValueError("Window sizes must be positive integers.")
    if fast_window >= slow_window:
        raise ValueError("fast_window must be smaller than slow_window.")

    fast_sma = prices.rolling(fast_window).mean()
    slow_sma = prices.rolling(slow_window).mean()
    signal = (fast_sma > slow_sma).astype(int)
    return signal.fillna(0)
