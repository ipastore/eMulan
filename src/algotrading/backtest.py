from __future__ import annotations

import pandas as pd


def run_backtest(prices: pd.Series, signal: pd.Series) -> pd.DataFrame:
    """
    Simple daily backtest with long/cash exposure.

    Uses prior-day signal as next-day position to avoid look-ahead bias.
    """
    if len(prices) == 0:
        raise ValueError("Price series is empty.")
    if not prices.index.equals(signal.index):
        raise ValueError("prices and signal must share the same index.")

    returns = prices.pct_change().fillna(0)
    position = signal.shift(1).fillna(0)
    strategy_returns = position * returns

    equity_curve = (1 + strategy_returns).cumprod()
    benchmark_curve = (1 + returns).cumprod()

    result = pd.DataFrame(
        {
            "price": prices,
            "signal": signal,
            "position": position,
            "returns": returns,
            "strategy_returns": strategy_returns,
            "equity_curve": equity_curve,
            "benchmark_curve": benchmark_curve,
        }
    )
    return result


def summarize_performance(result: pd.DataFrame) -> dict[str, float]:
    """Return key backtest performance metrics."""
    strategy_returns = result["strategy_returns"]
    benchmark_returns = result["returns"]

    total_return = result["equity_curve"].iloc[-1] - 1
    benchmark_return = result["benchmark_curve"].iloc[-1] - 1
    annualization = 252
    volatility = strategy_returns.std() * (annualization ** 0.5)
    sharpe = 0.0
    if volatility > 0:
        sharpe = (strategy_returns.mean() * annualization) / volatility

    rolling_max = result["equity_curve"].cummax()
    drawdown = (result["equity_curve"] / rolling_max) - 1
    max_drawdown = drawdown.min()

    return {
        "total_return": float(total_return),
        "benchmark_return": float(benchmark_return),
        "annualized_volatility": float(volatility),
        "sharpe_ratio": float(sharpe),
        "max_drawdown": float(max_drawdown),
    }
