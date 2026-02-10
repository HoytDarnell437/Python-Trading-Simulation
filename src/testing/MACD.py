# testing implementation of the Moving Average Convergence/ Divergence algorithm

def macd(price: float):
    # macd function implementation

    signal = ema(price, 9)
    ema12 = ema(price, 12)
    ema26 = ema(price, 26)

    print("ema12: ", ema12)
    print("ema26: ", ema26)

    difference12_16 = ema12 - ema26

    print("difference12_16: ", difference12_16)

    results = 5
    return(results, signal)


prevEMA = [0.0,0.0,0.0]
smoothing1 = [1/5, 2/13, 2/27]
smoothing2 = [4/5, 11/13, 25/27]

def ema(price: float, periods: int)->float:
    # estimated moving average function implementation
    if periods > 12:
        prevEMA[2] = smoothing1[2] * price + smoothing2[2] * prevEMA[2]
        return(prevEMA[2])
    
    elif periods > 9:
        prevEMA[1] = smoothing1[1] * price + smoothing2[1] * prevEMA[1]
        return(prevEMA[1])
    
    else:
        prevEMA[0] = smoothing1[0] * price + smoothing2[0] * prevEMA[0]
        return(prevEMA[0])