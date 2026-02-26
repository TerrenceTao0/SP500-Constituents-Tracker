from tracker import constituents_tracker
from datetime import datetime as dt

# 

if __name__ == "__main__":
    # Create tracker instance for specified universe.
    sp500_tracker = constituents_tracker(universe_file="sp500_history.csv", date_format="%Y-%m-%d")

    # Retrieve constituents for a given date.
    example_date = dt(2000, 12, 25)
    constituents = sp500_tracker.get(example_date)

    print(constituents)

    