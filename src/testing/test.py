import yfinance as yf
from MACD import macd

google = yf.Ticker("GOOG")

prices = [1.0,2.5,2.4,2.6,3.0,2.7,3.2,8.0,9.0,10.0,11.0,12.0,13.0,14.0,15.0,16.0,17.0,18.0,19.0,20.0,21.0,22.0,23.0,24.0,25.0,26.0]

previousResults = 0

previousSignal = 0

for price in prices:
    previousResults, previousSignal = macd(price)





print("Results: ", previousResults, "\nSignal: ", previousSignal)

