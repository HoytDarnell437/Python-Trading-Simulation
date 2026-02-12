# import libraries
import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np 

# import other files
from testMACD import macd
from testRSI import rsi
from testATR import atr

while True:

    stockSymbol = input("Input stock symbol: ")

    data = yf.download(stockSymbol, start="2024-02-11", end="2026-02-11") # CHANGE THESE DATES FOR TESTING TIMEFRAMES 
    closePrices = data["Close"][stockSymbol].tolist()
    highPrices = data["High"][stockSymbol].tolist()
    lowPrices = data["Low"][stockSymbol].tolist()

    startingCapital = 1000
    capital = 1000 # in dollars

    x = np.linspace(0, len(closePrices), len(closePrices), True)


    fig, ax = plt.subplots()
    startPrice = closePrices[0]
    risk = 1 # percent
    shares = 0
    stop = 0
    sharesString = ""
    totalChange = 0
    amountAllowed = 0
    previousResults = 0
    previousSignal = 0
    hasBought = False
    relativeStrengthIndex = 0
    atrResults = 1
    buyPrice = 0
    high = 0
    y2 = []
    y3 = []
    i = 0

    for price in closePrices:
        # IMPORTANT action is only valid after the first ~30 iterations
        # calculate macd
        previousResults, previousSignal, action = macd(price, previousResults, previousSignal)
        y2 += [previousResults]
        y3 += [previousSignal]
        riskPerTrade = capital * risk * 0.01

        if highPrices[i] > high: high = highPrices[i]

        if i > 50 and action != 0:
            #relativeStrengthIndex = rsi(closePrices[i - 15 : i])
            #atrResults = atr(highPrices[i - 15 : i], lowPrices[i - 15 : i], closePrices[i - 16 : i - 1])

            if (action == 1 or price <= stop) and hasBought:
                ax.scatter(i, price, color='red',marker='v')
                capital += shares * price - shares * buyPrice
                hasBought = False
                buyPrice = 0
            elif action == 2 and (not hasBought):
                ax.scatter(i, price, color='green',marker='^')
                shares = capital / price
                stop = max(stop, price * 0.95)
                hasBought = True
                buyPrice = price

        i += 1

    totalChange = capital - startingCapital

    print("Stock: ", stockSymbol)
    print("Percent Gain in Asset Value: ", f"{(100 * totalChange / startingCapital):.2f}", "%")
    print("Percent Gain in Stock Value: ", f"{(100 * (closePrices[-1] - startPrice) / startPrice):.2f}", "%")
    ax.plot(x, closePrices)
    ax.plot(x, y2)
    ax.plot(x, y3)
    plt.show()