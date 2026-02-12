# import libraries
import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np 

# import other files
from testMACD import macd
from testRSI import rsi
from testATR import atr
from testTrade import trade

while True:

    stockSymbol = input("Input stock symbol: ")

    data = yf.download(stockSymbol, start="2024-02-11", end="2026-02-11") # CHANGE THESE DATES FOR TESTING TIMEFRAMES 
    closePrices = data["Close"][stockSymbol].tolist()
    highPrices = data["High"][stockSymbol].tolist()
    lowPrices = data["Low"][stockSymbol].tolist()


    # change these variables
    prices = closePrices
    startingCapital = 1000
    capital = 1000 # in dollars
    risk = 1 # percent

    x = np.linspace(0, len(prices), len(prices), True)
    fig, ax = plt.subplots()

    startPrice = prices[0]
    stop = 0
    totalChange = 0
    amountAllowed = 0
    previousResults = 0
    previousSignal = 0
    relativeStrengthIndex = 0
    atrResults = 1
    buyPrice = 0
    high = 0
    y2 = []
    y3 = []
    i = 0

    for price in prices:
        # IMPORTANT action is only valid after the first ~30 iterations
        # calculate macd
        previousResults, previousSignal, action = macd(price, previousResults, previousSignal)
        y2 += [previousResults]
        y3 += [previousSignal]
        riskPerTrade = capital * risk * 0.01

        if i > 50 and action != 0:

            if action == 1 or price <= stop:
                ax.scatter(i, price, color='red',marker='v')
                capital += shares * price - shares * buyPrice
            elif action == 2:
                ax.scatter(i, price, color='green',marker='^')
                shares = capital / price
                stop = max(stop, price * 0.95)

        i += 1

    totalChange = capital - startingCapital

    print("Stock: ", stockSymbol)
    print("Percent Gain in Asset Value: ", f"{(100 * totalChange / startingCapital):.2f}", "%")
    print("Percent Gain in Stock Value: ", f"{(100 * (prices[-1] - startPrice) / startPrice):.2f}", "%")
    ax.plot(x, prices)
    ax.plot(x, y2)
    ax.plot(x, y3)
    plt.show()