# main loop for Testing trading algorithms. Algorithms currently implemented: macd, rsi, 
# import libraries
import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np 

# import other files
from algorithms.macd import macd
from algorithms.rsi import rsi
from trade import trade

while True:

    # get input from user
    stockSymbol = input("Input stock symbol: ").upper()
    algorithm = input("Input Algorithm Key (0: macd, 1: rsi): ")
    
    # import stock data
    ticker = yf.Ticker(stockSymbol)
    data = ticker.history(start = "2025-01-11", interval = "1h") # date to start aquiring data and time interval between samples
    closePrices = data["Close"].tolist()


    # change these variables
    prices = closePrices
    startingCapital = 1000 # in USD
    risk = 1 # percent
    macdSensitivity = 0

    # graphing setup
    x = np.linspace(0, len(prices), len(prices), True)
    fig, ax = plt.subplots()

    # loop variables
    totalChange = 0
    capital = startingCapital
    i = 0

    # main calculation loop
    for price in prices:
        # determine what the user wishes to test
        if algorithm == 0:
            print("macd")
        elif algorithm == 1:
            print("rsi")

        # send action to trade function
        if i > 30 and action != 0:
            capital += trade(price, capital, action, ax, i)
        elif i == (len(prices) - 1):
            capital += trade(price, capital, 1, ax, i) # ensure the stocks are sold on last iteration

        i += 1

    totalChange = capital - startingCapital

    # output data on graph and in terminal
    print("Stock: ", stockSymbol)
    print("Percent Gain in Asset Value: ", f"{(100 * totalChange / startingCapital):.2f}", "%")
    print("Percent Gain in Stock Value: ", f"{(100 * (prices[-1] - prices[0]) / prices[0]):.2f}", "%")
    ax.plot(x, prices)
    plt.show()