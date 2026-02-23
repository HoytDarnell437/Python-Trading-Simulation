def aroon(price: float, period: int = 25) -> int:
    global previousAroon
    priceList.insert(0, price)
    
    if len(priceList) < period:
        aroonList.append(0)
        return 0
    
    if len(priceList) > period:
        priceList.pop()

    subset = priceList[:period]
    high_val = low_val = subset[0]
    high_idx = low_idx = 1

    for i, p in enumerate(subset[1:], 2):
        if p > high_val:
            high_val = p
            high_idx = i
        if p < low_val:
            low_val = p
            low_idx = i

    aroon = 100 * (low_idx - high_idx) / period  # equivalent to aroonUp - aroonDown
    aroonList.append(aroon)

    if aroon >= 0 and previousAroon < 0:
        previousAroon = aroon
        return 2
    elif aroon <= 0 and previousAroon > 0:
        previousAroon = aroon
        return 1
    else:
        previousAroon = aroon
        return 0




previousAroon = 0.0
priceList = []
aroonList = [] # list that is graphed