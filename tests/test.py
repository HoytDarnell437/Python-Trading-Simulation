# import libraries
import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np 

# import other files
from testMACD import macd
from testRSI import rsi

while True:

    stockSymbol = input("Input stock symbol: ")

    data = yf.download(stockSymbol, start="2024-02-11", end="2025-02-11") # CHANGE THESE DATES FOR TESTING TIMEFRAMES 
    closePrices = data["Close"][stockSymbol].tolist()
    openPrices = data["Open"][stockSymbol].tolist()

    prices = []
    for i in range(len(closePrices)):
        prices += [openPrices[i]]
        prices += [closePrices[i]]


    numberShares = 1

    startingCapital = 100
    capital = 100 # in dollars

    x = np.linspace(0, len(prices), len(prices), True)


    fig, ax = plt.subplots()
    startPrice = prices[0]
    shares = 0
    sharesString = ""
    totalChange = 0
    previousResults = 0
    previousSignal = 0
    hasBought = False
    buyPrice = 0
    y2 = []
    y3 = []
    i = 0

    for price in prices:
        # IMPORTANT action is only valid after the first ~30 iterations
        # calculate macd
        previousResults, previousSignal, action = macd(price, previousResults, previousSignal)
        y2 += [previousResults]
        y3 += [previousSignal]

        # calculate rsi
        if i > 14:
            relativeStrengthIndex = rsi(prices[i-15:i])

        if i > 26 and action != 0:
            if action == 1 and hasBought and relativeStrengthIndex > 30:
                ax.scatter(i, price, color='red',marker='v')
                totalChange += shares * price - shares * buyPrice
                capital = shares * price 
                hasBought = False
                buyPrice = 0
            elif action == 2 and (not hasBought) and relativeStrengthIndex < 70:
                ax.scatter(i, price, color='green',marker='^')
                shares = (capital / price)
                hasBought = True
                buyPrice = price

        i += 1


    print("Stock: ", stockSymbol)
    print("Percent Gain in Asset Value: ", f"{(100 * totalChange / startingCapital):.2f}", "%")
    print("Percent Gain in Stock Value: ", f"{(100 * (prices[-1] - startPrice) / startPrice):.2f}", "%")
    ax.plot(x, prices)
    ax.plot(x, y2)
    ax.plot(x, y3)
    #plt.show()


