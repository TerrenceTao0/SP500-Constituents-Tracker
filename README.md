# SP500-Constituents-Tracker
Allows you to find the constituents of the SP500 at a specific date. This can be used to eliminate survivorship bias in backtesting. This also works for any universe with a column for "date" and a column for "tickers". The code will let you define the names for each column if they are named differently.

## Initialisation 
<pre>
    
from tracker import ConstituentsTracker

tracker = ConstituentsTracker(
    universe_file="data/sp500_history.csv",    # [REQUIRED] CSV file containing historical constituents
    date_format="%Y-%m-%d",**                  # [REQUIRED] Format of your date column
    tickers_column="tickers",**                # [OPTIONAL] Name of the column containing tickers
    ticker_seperator=","**                     # [OPTIONAL] Character separating the list of tickers
)

## Functions 
tickers = tracker.get_tickers_at(
  "2000-01-01"                                 # [REQUIRED] Date 
)
# Output: ['AAPL', 'MSFT', 'IBM', ...]

exists = tracker.ticker_exists(
  "AAPL"                                       # [REQUIRED] Ticker 
  "2000-01-01"                                 # [REQUIRED] Date
)
# Output: True (Boolean)

universe_size = tracker.universe_size_at(
  "2000-01-01"                                 # [REQUIRED] Date
)
# Output: 492 

date = tracker.ticker_first_seen(
  "AAPL"                                       # [REQUIRED] Ticker 
)
# Output: 492 
    
</pre>
