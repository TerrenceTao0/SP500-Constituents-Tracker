import datetime as dt 
from tracker import ConstituentsTracker

# 

if __name__ == "__main__":
    # Create tracker instance for specified universe.
    sp500_tracker = ConstituentsTracker(universe_file="sp500_history.csv", date_format="%Y-%m-%d")

    # Example date to query.
    example_date = dt.date(2000, 12, 25)
    
    # Retrieve constituents of universe at a given date.
    tickers = sp500_tracker.get_tickers_at(example_date)

    # Check if a given ticker was part of the universe at a given date.
    exists = sp500_tracker.ticker_exists("AAPL", example_date)

    # Get the size of the universe at a given date.
    universe_size = sp500_tracker.universe_size_at(example_date)

    # Check the first date a given ticker was part of the universe.
    date = sp500_tracker.ticker_first_seen("AAPL")

    # Check the last date a given ticker was part of the universe.
    date = sp500_tracker.ticker_last_seen("AAPL")

    print(date)
