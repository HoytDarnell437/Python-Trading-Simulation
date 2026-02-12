# variables that need to be kept between calls
shares = 0
hasBought = False
def trade(price: float, signal: int, capital: float):
    global hasBought, shares
    if signal == 0: # neither buy nor sell
        return 0
    elif signal == 1 and hasBought: # sell
        priceChange = shares * price
        hasBought = False
        return priceChange
    elif not hasBought: # buy
        shares = capital / price
        hasBought = True
        priceChange = -(shares * price)
        return priceChange
    