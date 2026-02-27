#!/usr/bin/env python3
from __future__ import annotations

import argparse

from algotrading.backtest import run_backtest, summarize_performance
from algotrading.data import fetch_close_prices
from algotrading.strategy import sma_crossover_signals


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Run SMA crossover backtest.")
    parser.add_argument("--symbol", default="AAPL", help="Ticker symbol (default: AAPL)")
    parser.add_argument("--start", default="2020-01-01", help="Start date YYYY-MM-DD")
    parser.add_argument("--end", default="2024-12-31", help="End date YYYY-MM-DD")
    parser.add_argument("--fast", type=int, default=20, help="Fast SMA window")
    parser.add_argument("--slow", type=int, default=50, help="Slow SMA window")
    return parser.parse_args()


def main() -> None:
    args = parse_args()

    prices = fetch_close_prices(args.symbol, args.start, args.end)
    signal = sma_crossover_signals(prices, fast_window=args.fast, slow_window=args.slow)
    result = run_backtest(prices, signal)
    metrics = summarize_performance(result)

    print(f"Backtest for {args.symbol} ({args.start} -> {args.end})")
    for key, value in metrics.items():
        print(f"{key:>22}: {value:.4f}")


if __name__ == "__main__":
    main()
