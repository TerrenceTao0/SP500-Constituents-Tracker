import pandas as pd 
from datetime import datetime as dt

#

class ConstituentsTracker():
    def __init__(self, universe_file, date_format="%Y-%m-%d", tickers_column="tickers", ticker_seperator=",", date_column="date"):
        df = pd.read_csv(universe_file)
        df[date_column] = pd.to_datetime(df[date_column], format=date_format).dt.date

        self.universe_df = df.sort_values(date_column).set_index(date_column)
        self.tickers_column = tickers_column
        self.ticker_seperator = ticker_seperator
        self.date_column = date_column


    def get_tickers_at(self, date):
        idx = self.universe_df.index.asof(date)

        if (pd.isna(idx)):
            return []
        

        return self.universe_df.loc[idx, self.tickers_column].split(self.ticker_seperator)
    

    def ticker_exists(self, queried_ticker, date):
        tickers = self.get_tickers_at(date)

        for ticker in tickers:
            if (ticker == queried_ticker):
                return True 
            

        return False 
        

    def universe_size_at(self, date):
        tickers = self.get_tickers_at(date)

        if (tickers):
            return len(tickers)
        
        else:
            return 0 


    def ticker_first_seen(self, ticker):
        for date in self.universe_df.index:
            if (ticker in self.get_tickers_at(date)):
                return date
            

        return None


    def ticker_last_seen(self, ticker):
        last_date = None

        for date in self.universe_df.index:
            if (ticker in self.get_tickers_at(date)):
                last_date = date 

            elif (last_date):
                return last_date 
            

        return last_date
    
