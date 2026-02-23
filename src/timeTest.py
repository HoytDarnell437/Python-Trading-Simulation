# main loop for Testing trading algorithms. Algorithms currently implemented: macd, rsi, goog
# import libraries
import random as r
from timeit import timeit

# import other files
from algorithms.macd import macd
from algorithms.rsi import rsi
from algorithms.aroon import aroon

# change these variables
macdSensitivity = 0
randomPrice = r.randrange(50,600)
iterations = 1000000

# main function implementation
def timeTest():

    # get input from user
    algorithm = int(input("Input Algorithm Key (macd: 0, rsi: 1, aroon: 2): "))

    # choose proper iterator
    if algorithm == 0:
        print(round(timeit("macd(randomPrice,macdSensitivity)", "from algorithms.macd import macd\nfrom __main__ import macdSensitivity, randomPrice", number= iterations)/iterations * (10 ** 6),4), "Microseconds") 
    elif algorithm == 1:
        print(round(timeit("rsi(randomPrice)", "from algorithms.rsi import rsi\nfrom __main__ import randomPrice", number= iterations)/iterations * (10 ** 6),4), "Microseconds") 
    elif algorithm == 2:
        print(round(timeit("aroon(randomPrice)", "from algorithms.aroon import aroon\nfrom __main__ import randomPrice", number= iterations)/iterations * (10 ** 6),4), "Microseconds") 

# call main function
while __name__ == "__main__":
    timeTest()