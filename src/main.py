# main loop for Testing trading algorithms. Algorithms currently implemented: macd, rsi, goog
# import libraries
import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np 
from timeit import timeit

# import other files
from algorithms.macd import macd, signalList, macdList
from algorithms.rsi import rsi, rsiList
from algorithms.aroon import aroon, aroonList
from trade import trade

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

    # graphing setup
    x = np.linspace(0, len(prices), len(prices), True)
    fig, ax = plt.subplots()
    fig, ax1 = plt.subplots()
    fig, ax2 = plt.subplots()

    # loop variables
    totalChange = 0
    capital = startingCapital
    i = 0

    # main calculation loop
    for price in prices:
        # determine what the user wishes to test
        action = 0
        if algorithm == 0: # call macd 
            action = macd(price, 1)
        elif algorithm == 1: # call rsi
            action = rsi(price)
        elif algorithm == 2: # call aroon
            action = aroon(price)

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
    
    ax.plot(x, prices, label="Price") # plot stock prices
    ax1.plot(x, prices, label="Price") # plot stock prices
    if algorithm == 0: # plot macd and signal
        ax.plot(x, macdList, label="MACD")
        ax2.plot(x, macdList, label="MACD")
        macdList.clear()
        ax.plot(x, signalList, label="Signal")
        ax2.plot(x, signalList, label="Signal")
        signalList.clear()
    if algorithm == 1: # plot rsi
        ax.plot(x, rsiList, label="RSI")
        ax2.plot(x, rsiList, label="RSI")
        rsiList.clear()
    if algorithm == 2: # plot aroon
        ax.plot(x, aroonList, label="AROON")
        ax2.plot(x, aroonList, label="AROON")
        aroonList.clear()

    ax.grid(True)
    ax1.grid(True)
    ax2.grid(True)
    plt.legend()
    plt.show()