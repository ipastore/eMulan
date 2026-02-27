# Algorithmic Trading Starter Project

Lightweight Python starter for researching and backtesting simple trading ideas.

## What is included
- Git-ready project structure
- Price download helper (`yfinance`)
- SMA crossover strategy
- Basic vectorized backtest engine
- CLI script to run a backtest
- Minimal tests

## Project structure
```text
.
├── pyproject.toml
├── requirements.txt
├── scripts/
│   └── run_backtest.py
├── src/
│   └── algotrading/
│       ├── __init__.py
│       ├── backtest.py
│       ├── data.py
│       └── strategy.py
└── tests/
    └── test_strategy.py
```

## Quick start
1. Create and activate a virtual environment:
   ```bash
   python3 -m venv .venv
   source .venv/bin/activate
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   pip install -e .
   ```
3. Run a sample backtest:
   ```bash
   python scripts/run_backtest.py --symbol AAPL --start 2020-01-01 --end 2024-12-31 --fast 20 --slow 50
   ```
4. Run tests:
   ```bash
   pytest
   ```

## Git usage
This folder is already initialized as a Git repository.

Initial commit:
```bash
git add .
git commit -m "Initial algorithmic trading scaffold"
```

Connect to a remote repository (GitHub/GitLab/Bitbucket):
```bash
git remote add origin <your-repo-url>
git push -u origin main
```

## Notes
- This is for research/education and not financial advice.
- Add risk management, transaction costs, slippage, and walk-forward validation before real deployment.
