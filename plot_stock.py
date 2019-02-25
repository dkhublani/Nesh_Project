# -*- coding: utf-8 -*-
"""
Created on Mon Feb 25 01:43:02 2019

@author: 19797
"""



from pandas_datareader import data
import matplotlib.pyplot as plt
import pandas as pd


def stock_trend(start, end, ticker):

    start_date = start
    end_date = end


    # User pandas_reader.data.DataReader to load the desired data. As simple as that.
    panel_data = data.DataReader( ticker, 'yahoo', start_date, end_date)


    # Getting just the adjusted closing prices. This will return a Pandas DataFrame
     # The index in this DataFrame is the major index of the panel_data.
    close = panel_data['Close']


    # Getting all weekdays between 01/01/2000 and 12/31/2016
    all_weekdays = pd.date_range(start=start_date, end=end_date, freq='B')
    
    
    # How do we align the existing prices in adj_close with our new set of dates?
    # All we need to do is reindex close using all_weekdays as the new index
    close = close.reindex(all_weekdays)
    
    # Reindexing will insert missing values (NaN) for the dates that were not present
    # in the original set. To cope with this, we can fill the missing by replacing them
    # with the latest available price for each instrument.
    close = close.fillna(method='ffill')
    
    # Get the MSFT timeseries. This now returns a Pandas Series object indexed by date.
    #msft = close.loc[:, 'EOG']
    
    
    # Plot everything by leveraging the very powerful matplotlib package
    fig, ax = plt.subplots(figsize=(16,9))
    
    ax.plot(close.index, close, label= ticker)
    #ax.plot(short_rolling_msft.index, short_rolling_msft, label='20 days rolling')
    #ax.plot(long_rolling_msft.index, long_rolling_msft, label='100 days rolling')
    
    ax.set_xlabel('Date')
    ax.set_ylabel('Price ($)')
    ax.legend()   


if __name__ == "__main__":
    x = input("Enter Start date in the yyyy-mm-dd format: ",)    
    y = input("Enter End date in the yyyy-mm-dd format: ",)    
    z = input("Enter Ticker: ",)    

    stock_trend(x, y, z)