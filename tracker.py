import pandas as pd 
from datetime import datetime as dt

#

class constituents_tracker():
    def __init__(self, universe_file, date_format="%Y-%m-%d"):
        df = pd.read_csv(universe_file)
        df["date"] = pd.to_datetime(df["date"], format=date_format)
        self.sp500_df = df.sort_values("date").set_index("date")


    def get(self, date):
        idx = self.sp500_df.index.asof(date)

        if (pd.isna(idx)):
            return []
        

        return self.sp500_df.loc[idx, "tickers"].split(",")
    

