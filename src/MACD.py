# testing implementation of the Moving Average Convergence/ Divergence algorithm

def macd(price: float, prevMACD: float, prevSignal: float, sensitivity: int):
    """
    Calculate MACD for given parameters intended for use inside of a loop
    
    :param price: Current price of stock
    :type price: float
    :param prevMACD: MACD calculated last iteration
    :type prevMACD: float
    :param prevSignal: Signal calculated last iteration
    :type prevSignal: float
    :param aggression: How aggressive you want the algorithm to be
    :type aggression: Int range 0-3
    :return: 0 is the default return 1 indicates selling is a good idea 2 indicates buying is a good idea
    :rtype: int
    """
    # macd function implementation
    global sensitivityDICT
    emaLow = ema(price, "emaLow", sensitivityDict[str(sensitivity)][1])
    emaHigh = ema(price, "emaHigh", sensitivityDict[str(sensitivity)][2])
    
    difference12_26 = emaLow - emaHigh
    results = difference12_26
    signal = ema(results, "signal", sensitivityDict[str(sensitivity)][0])

    if (prevMACD <= prevSignal) and (results > signal):
        action = 2
    elif (prevMACD >= prevSignal) and (results < signal):
        action = 1
    else:
        action = 0

    return action


prevEMA = {
    "emaLow": 0.0,
    "emaHigh": 0.0,
    "signal": 0.0
}

sensitivityDict = {
    '0': [18, 24, 52],
    '1': [9, 12, 26],
    '2': [5, 5, 35],
    '3': [3, 5, 13]
}

def ema(price: float, alphaKey: str, periods: int)->float:
    # estimated moving average function implementation
    global prevEMA
    alpha = 2 / (periods + 1) # smoothing constant

    prevEMA[alphaKey] = alpha * price + (1 - alpha) * prevEMA[alphaKey]
    return prevEMA[alphaKey]