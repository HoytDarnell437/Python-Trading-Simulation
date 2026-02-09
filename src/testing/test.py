import yfinance as yf

google = yf.Ticker("GOOG")

# Show Actions (dividends, splits)
google.actions

# Show Dividends
google.dividends

# Show Splits
google.splits

