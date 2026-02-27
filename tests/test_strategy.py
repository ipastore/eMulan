import pandas as pd

from algotrading.strategy import sma_crossover_signals


def test_sma_crossover_returns_binary_signal():
    prices = pd.Series([100, 101, 102, 103, 104, 103, 102, 101, 100, 99])
    signal = sma_crossover_signals(prices, fast_window=2, slow_window=3)

    assert set(signal.unique()).issubset({0, 1})
    assert len(signal) == len(prices)


def test_sma_crossover_rejects_invalid_windows():
    prices = pd.Series([100, 101, 102, 103, 104])

    try:
        sma_crossover_signals(prices, fast_window=5, slow_window=3)
    except ValueError:
        pass
    else:
        raise AssertionError("Expected ValueError when fast_window >= slow_window.")
