# SP500-Constituents-Tracker
Allows you to find the constituents of the SP500 and other useful information at specified dates. This can be used to eliminate survivorship bias in backtesting. This also works for any universe with a column for "date" and a column for "tickers". The code will let you define the names for each column if they are named differently. Note that the given SP500 constituents history data only goes as far back as 1996-01-02 and as recent as 2025-11-11

## Initialisation 
<pre>
from tracker import ConstituentsTracker

tracker = ConstituentsTracker(
    universe_file="data/sp500_history.csv",    # [REQUIRED] CSV file containing historical constituents
    date_format="%Y-%m-%d",                    # [OPTIONAL] Format of your date column
    tickers_column="tickers",                  # [OPTIONAL] Name of the column containing tickers
    ticker_seperator=","                       # [OPTIONAL] Character separating the list of tickers
    date_column="date"                         # [OPTIONAL] Name of the column containing dates
)
</pre>

## Functions 
<pre>
tickers = tracker.get_tickers_at(
  "2000-01-01"                                 # [REQUIRED] Date 
)
# Output: ['AAPL', 'MSFT', 'IBM', ...]
</pre>

<pre>
exists = tracker.ticker_exists(
  "AAPL"                                       # [REQUIRED] Ticker 
  "2000-01-01"                                 # [REQUIRED] Date
)
# Output: True (Boolean)
</pre>

<pre>
universe_size = tracker.universe_size_at(
  "2000-01-01"                                 # [REQUIRED] Date
)
# Output: 492 
</pre>

<pre>
date = tracker.ticker_first_seen(
  "AAPL"                                       # [REQUIRED] Ticker 
)
# Output: 1996-01-02 
</pre>

<pre>
date = tracker.ticker_last_seen(
  "AAPL"                                       # [REQUIRED] Ticker 
)
# Output: 2025-11-11 
</pre>
