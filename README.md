# Stock Portfolio Analysis

A Python-based tool to analyze stock portfolio performance, returns, and risk metrics.

## Features

- **Portfolio Performance Tracking**: Monitor gains/losses on individual stocks
- **Return Calculations**: Compute total return, annualized return, and daily returns
- **Risk Metrics**: Calculate volatility, Sharpe ratio, and maximum drawdown
- **Visualization**: Generate charts for portfolio allocation and performance trends
- **Data Export**: Export analysis results to CSV and Excel

## Project Structure

```
stock-portfolio-analysis/
├── README.md
├── requirements.txt
├── data/
│   ├── portfolio.csv          # Your portfolio holdings
│   └── stock_prices.csv       # Historical stock prices
├── src/
│   ├── portfolio_analysis.py  # Main analysis functions
│   ├── data_fetcher.py        # Fetch stock data from APIs
│   └── visualizations.py      # Charting and visualization
├── notebooks/
│   └── analysis_example.ipynb # Jupyter notebook with examples
└── output/
    ├── reports/               # Generated reports
    └── charts/                # Generated visualizations
```

## Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/as4102697-dot/Portfolio-Analysis-.git
   cd Portfolio-Analysis-
   ```

2. **Create a virtual environment**:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

## Quick Start

1. **Add your portfolio data** to `data/portfolio.csv`:
   ```csv
   symbol,quantity,purchase_price,purchase_date
   AAPL,10,150.00,2023-01-15
   MSFT,5,300.00,2023-02-20
   GOOGL,8,2500.00,2023-03-10
   ```

2. **Run the analysis**:
   ```bash
   python src/portfolio_analysis.py
   ```

3. **View results** in the `output/` directory

## Example Usage

```python
from src.portfolio_analysis import PortfolioAnalyzer

# Initialize analyzer
analyzer = PortfolioAnalyzer('data/portfolio.csv', 'data/stock_prices.csv')

# Calculate returns
total_return = analyzer.calculate_total_return()
print(f"Total Return: {total_return:.2f}%")

# Get risk metrics
sharpe_ratio = analyzer.calculate_sharpe_ratio()
print(f"Sharpe Ratio: {sharpe_ratio:.2f}")

# Generate visualizations
analyzer.plot_allocation()
analyzer.plot_performance()
```

## Data Sources

- **Stock Prices**: Yahoo Finance (via `yfinance`)
- **Market Data**: Alpha Vantage API (optional)

## Dependencies

- pandas
- numpy
- matplotlib
- plotly
- yfinance
- scikit-learn

See `requirements.txt` for full list.

## Next Steps

1. Add your portfolio data to `data/portfolio.csv`
2. Run `python src/portfolio_analysis.py` to generate initial analysis
3. Check `notebooks/analysis_example.ipynb` for detailed walkthroughs
4. Customize visualizations and metrics in `src/visualizations.py`

## Contributing

Feel free to fork, improve, and submit pull requests!

## License

MIT License - see LICENSE file for details
