import yfinance as yf
import pandas as pd

# Download Bitcoin Price data for the last 10 years
btc_data = yf.download("BTC-USD", period = "10y")

# Save the data to a csv file
btc_data.to_csv('btc_price.csv')

print("BTC price data downloaded and saved to btc_price.csv")




