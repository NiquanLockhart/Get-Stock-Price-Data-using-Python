In [2]: import pandas as pd
   ...: import yfinance as yf
   ...: import datetime
   ...: from datetime import date, timedelta
   ...: today = date.today()
   ...: 
   ...: d1 = today.strftime("%Y-%m-%d")
   ...: end_date = d1
   ...: d2 = date.today() - timedelta(days=360)
   ...: d2 = d2.strftime("%Y-%m-%d")
   ...: start_date = d2
   ...: 
   ...: data = yf.download('SPY',
   ...:                    start=start_date,
   ...:                    end=end_date,
   ...:                    progress=False)
   ...: print(data.head())
   ...: 
                  Open        High  ...   Adj Close     Volume
Date                                ...                       
2021-07-13  436.239990  437.839996  ...  429.483612   52911300
2021-07-14  437.399994  437.920013  ...  430.124512   64130400
2021-07-15  434.809998  435.529999  ...  428.655396   55126400
2021-07-16  436.010010  436.059998  ...  425.293152   75874700
2021-07-19  426.190002  431.410004  ...  419.012512  147987000
[5 rows x 6 columns]
