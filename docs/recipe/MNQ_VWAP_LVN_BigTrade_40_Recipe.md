# MNQ Strategy Recipe: VWAP + LVN + Big Trade Filter (40 Contracts)

## 1) Objective
Adapt the current MNQ approach into a rule-based intraday strategy that combines:
- `VWAP` as fair-value anchor.
- `LVN (Low Volume Nodes)` as low-acceptance price zones.
- `Big trade filter` using prints of `>= 40` contracts for participation confirmation.

This recipe follows the framework in `docs/algoritmic_tradoing_theory/` (Modules 1-5).

## 2) Theory Behind The Edge

### 2.1 Behavioural and market structure rationale
- Module 1 (Behavioural finance): markets can overreact/underreact; flow confirmation helps avoid purely emotional moves.
- Module 1 (Momentum vs mean reversion): this setup allows both, but only with explicit rules.
- Module 2 (Systematic trading): predefined rules reduce discretionary bias and improve discipline.
- Module 2/3 (Futures focus): futures are liquid/scalable, but leverage and intraday risk must be controlled.
- Module 2/3 (HFT/microstructure): trade size and execution quality matter; large prints can signal informed urgency.

### 2.2 Modelling and validation rationale
- Module 3: start from candidate predictors, backtest, and validate with out-of-sample (OOS) testing.
- Module 3/5: include slippage and transaction costs; do not trust in-sample performance alone.
- Module 5: avoid “too good to be true” results; verify model explanation, robustness, and drawdown behavior.
- Module 4: optimize cautiously; do not burn OOS by repeatedly tuning to it.

## 3) Strategy Specification

### 3.1 Market and session
- Instrument: `MNQ` (Micro Nasdaq-100 futures).
- Session: US regular trading hours.
- No trading window: first `15-30` minutes after open.
- No trading during high-impact macro releases (CPI, FOMC, NFP).

### 3.2 Indicators and inputs
- `Session VWAP` (resets daily).
- `Volume Profile` zones: prior-session LVNs and developing-session LVNs.
- `Big trade filter`: a qualifying print is an aggressive trade of `>= 40 contracts`.
- Setup is valid only if qualifying prints appear in the intended direction near the LVN/VWAP interaction area.

### 3.3 Long setup (continuation/reclaim type)
1. Price is above VWAP, or reclaims VWAP and holds.
2. Pullback reaches an LVN zone near VWAP.
3. Tape shows at least one aggressive buy print `>= 40` contracts in that zone.
4. Enter long on confirmation (break of setup candle high or equivalent trigger).

### 3.4 Short setup (continuation/reject type)
1. Price is below VWAP, or loses VWAP and fails to recover.
2. Retracement reaches an LVN zone near VWAP.
3. Tape shows at least one aggressive sell print `>= 40` contracts in that zone.
4. Enter short on confirmation (break of setup candle low or equivalent trigger).

### 3.5 Risk and trade management (adapted from your current MNQ recipe)
- Baseline size: `1 MNQ contract`.
- Conservative stop: `25 points` (`$50` risk).
- Moderate stop: `37.5 points` (`$75` risk), only in higher volatility sessions.
- Minimum target: `2R` (risk-reward at least 1:2).
- Break-even rule: move stop to entry at `+1R`.
- Daily loss limit: `75 points` (`$150`) then stop trading for the day.

## 4) Practical Insights (Strategy + Theory)

### 4.1 Why VWAP + LVN + big trades can work
- VWAP approximates the day’s fair value used by institutions.
- LVNs represent low acceptance; price often moves fast through them unless new participation appears.
- Big prints (`>= 40`) add evidence that real size is active, reducing weak/noise entries.

### 4.2 Failure regimes to expect
- Choppy, low-range sessions around VWAP (many false reclaims/rejections).
- News-driven spikes (slippage and discontinuous fills).
- Regime shifts where historical flow behavior changes.

### 4.3 How to keep it aligned with Oxford methodology
- Define predictors explicitly: distance to VWAP, LVN interaction state, and count/intensity of qualifying big prints.
- Backtest with realistic fees and slippage.
- Use OOS split (alternating years is acceptable per course guidance).
- Require robustness: OOS degradation not excessively larger than in-sample, plus positive behavior under slippage stress tests (for example +10% to +20%, and severe stress case).
- Evaluate with risk-adjusted metrics: Sharpe, Sortino, max drawdown, returns-to-drawdown.

## 5) Implementation Notes
- Keep first version simple (few parameters) to reduce overfitting risk.
- Log every trade with setup type, VWAP distance, LVN reference, number/size of qualifying prints, and slippage at entry/exit.
- Reassess monthly; if live behavior diverges materially from simulation assumptions, reduce size and review model validity.

## 6) Final Warning
This is a research framework, not financial advice. For live deployment, treat execution risk, slippage, and drawdown control as first-class constraints.
