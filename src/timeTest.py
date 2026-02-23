# main loop for Testing trading algorithms. Algorithms currently implemented: macd, rsi, goog
# import libraries
import random as r
import yfinance as yf
import pandas as pd
import numpy as np 
from timeit import timeit

# import other files
from algorithms.macd import macd
from algorithms.rsi import rsi
from algorithms.aroon import aroon

while True:

    # get input from user
    stockSymbol = input("Input stock symbol: ").upper()
    algorithm = int(input("Input Algorithm Key (macd: 0, rsi: 1, aroon: 2): "))

    
    # import stock data
    ticker = yf.Ticker(stockSymbol)
    data = ticker.history(start = "2025-01-11", interval = "1d") # date to start aquiring data and time interval between samples
    closePrices = data["Close"].tolist()


    # change these variables
    prices = closePrices
    startingCapital = 1000 # in USD
    risk = 1 # percent
    macdSensitivity = 0
    randomPrice = r.randrange(50,600)
    iterations = 1000000


    # choose proper iterator
    if algorithm == 0:
        print(round(timeit("macd(randomPrice,macdSensitivity)", "from algorithms.macd import macd\nfrom __main__ import macdSensitivity, randomPrice", number= iterations)/iterations * (10 ** 9),2), "Nanoseconds") 
    elif algorithm == 1:
        print(round(timeit("rsi(randomPrice)", "from algorithms.rsi import rsi\nfrom __main__ import randomPrice", number= iterations)/iterations * (10 ** 9),2), "Nanoseconds") 
    elif algorithm == 2:
        print(round(timeit("aroon(randomPrice)", "from algorithms.aroon import aroon\nfrom __main__ import randomPrice", number= iterations)/iterations * (10 ** 9),2), "Nanoseconds") 