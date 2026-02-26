import pandas as pd 
import datetime as dt

#

class ConstituentsTracker():
    def to_date(self, input_date):
        if (isinstance(input_date, dt.date)):
            return input_date

        elif (isinstance(input_date)):
            return dt.strptime(input_date, self.date_format).date()
        
        elif (isinstance(input_date, dt)):
            return input_date.date()
        
        elif (isinstance(input_date, pd.Timestamp)):
            return input_date.date()
        
        else:
            raise ValueError("Unsupported date format. Please provide a string, datetime, or pandas Timestamp.")


    def clear_cache(self):
        self.cached_results = {
            "get_tickers_at": {},
            "ticker_exists": {},
            "universe_size_at": {},   
            "ticker_first_seen": {},
            "ticker_last_seen": {},
            "ticker_lifetime": {}
        }


    def __init__(self, universe_file, date_format="%Y-%m-%d", tickers_column="tickers", ticker_seperator=",", date_column="date"):
        if (not universe_file):
            raise ValueError("Universe file path must be provided.")


        df = pd.read_csv(universe_file)
        df[date_column] = pd.to_datetime(df[date_column], format=date_format).dt.date

        self.universe_df = df.sort_values(date_column).set_index(date_column)
        self.tickers_column = tickers_column
        self.ticker_seperator = ticker_seperator
        self.date_column = date_column
        self.date_format = date_format
        self.clear_cache()


    def get_tickers_at(self, date):
        if (not date):
            raise ValueError("Date must be provided.")


        date = self.to_date(date)

        if (date in self.cached_results["get_tickers_at"]):
            return self.cached_results["get_tickers_at"][date]


        idx = self.universe_df.index.asof(date)

        if (pd.isna(idx)):
            return []
        

        tickers = self.universe_df.loc[idx, self.tickers_column].split(self.ticker_seperator)
        self.cached_results["get_tickers_at"][date] = tickers

        return tickers
    

    def ticker_exists(self, queried_ticker, date):
        if (not queried_ticker):
            raise ValueError("Ticker must be provided.")


        if (not date):
            raise ValueError("Date must be provided.")
        

        date = self.to_date(date)
        date_str = date.strftime("%Y-%m-%d")
        cache_string = f"{queried_ticker}_{date_str}"

        if (cache_string in self.cached_results["ticker_exists"]):
            return self.cached_results["ticker_exists"][cache_string]


        tickers = self.get_tickers_at(date)

        for ticker in tickers:
            if (ticker == queried_ticker):
                self.cached_results["ticker_exists"][cache_string] = True   

                return True 
            

        self.cached_results["ticker_exists"][cache_string] = False   
            
        return False 
        

    def universe_size_at(self, date):
        if (not date):
            raise ValueError("Date must be provided.")


        date = self.to_date(date)
        date_str = date.strftime("%Y-%m-%d")
        cache_string = date_str

        if (cache_string in self.cached_results["universe_size_at"]):
            return self.cached_results["universe_size_at"][cache_string]
        

        tickers = self.get_tickers_at(date)

        if (tickers):
            n = len(tickers)
            self.cached_results["universe_size_at"][cache_string] = n

            return n
        
        else:
            return 0 


    def ticker_first_seen(self, ticker):
        if (not ticker):
            raise ValueError("Ticker must be provided.")


        cache_string = ticker

        if (cache_string in self.cached_results["ticker_first_seen"]):
            return self.cached_results["ticker_first_seen"][cache_string]


        for date in self.universe_df.index:
            if (ticker in self.get_tickers_at(date)):
                self.cached_results["ticker_first_seen"][cache_string] = date

                return date
            

        return None


    def ticker_last_seen(self, ticker):
        if (not ticker):
            raise ValueError("Ticker must be provided.")


        cache_string = ticker 

        if (cache_string in self.cached_results["ticker_last_seen"]):
            return self.cached_results["ticker_last_seen"][cache_string]    
        

        last_date = None

        for date in self.universe_df.index:
            if (ticker in self.get_tickers_at(date)):
                last_date = date 

            elif (last_date):
                self.cached_results["ticker_last_seen"][cache_string] = last_date   

                return last_date 
            

        self.cached_results["ticker_last_seen"][cache_string] = last_date   

        return last_date
    

    def ticker_lifetime(self, ticker):
        if (not ticker):
            raise ValueError("Ticker must be provided.")


        cache_string = ticker

        if (cache_string in self.cached_results["ticker_lifetime"]):
            return self.cached_results["ticker_lifetime"][cache_string]


        first_date = self.ticker_first_seen(ticker)
        last_date = self.ticker_last_seen(ticker)

        if (first_date and last_date):
            days = (last_date - first_date).days
            self.cached_results["ticker_lifetime"][cache_string] = days

            return days
        
        else:
            return None
    
