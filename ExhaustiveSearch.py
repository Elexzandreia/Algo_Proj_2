# This is where we'll have the function(s) for part A, Exhaustive Search Approach.  
from itertools import combinations

class Stock:
    def __init__(self, numberOfStocks, cost):
        self.numberOfStocks = numberOfStocks
        self.cost = cost


def readStockDataFromFile(fileName):
    allStocks = []
    maxAmounts = []

    with open(fileName, 'r') as file:
        while True:
            line = file.readline()
            if not line.strip():
                break

            numberOfStocks = int(line.strip())
            stockData = eval(file.readline().strip())
            currentSetStocks = []

            for data in stockData:
                currentSetStocks.append(Stock(*data))

            allStocks.append(currentSetStocks) 
            maxAmounts.append(int(file.readline().strip()))
            file.readline()

    return allStocks, maxAmounts

def stockOptimization(maxAmountAllowed, stocks):
    currentBest = None
    for i in range(len(stocks) + 1):
        for candidateStocks in combinations(stocks, i):
            if verifyCandidateStocks(maxAmountAllowed, candidateStocks):
                if currentBest is None or totalNumberOfStocks(candidateStocks) > totalNumberOfStocks(currentBest): 
                    currentBest = candidateStocks
    return currentBest

def verifyCandidateStocks(maxAmountAllowed, candidateStocks):
    totalCostOfCandidateStocks = sum(stock.cost for stock in candidateStocks) 
    if totalCostOfCandidateStocks <= maxAmountAllowed: 
        return True
    else:
        return False

def totalNumberOfStocks(candidateStocks):
    totalStockNumber = sum(stock.numberOfStocks for stock in candidateStocks)
    return totalStockNumber



allStocks, maxAmounts = readStockDataFromFile('input.txt')

for setIndex, stocks in enumerate(allStocks):
    example1 = stockOptimization(maxAmounts[setIndex], stocks)
    result1 = 0
    print()
    for stock in example1:
        print(f"Stocks selected: ({stock.numberOfStocks}, {stock.cost})")
        result1 += stock.numberOfStocks
    print(f"Max Amount for Set {setIndex + 1}: {maxAmounts[setIndex]}")
    print(f"Result to be printed to output.txt: {result1}\n")

# Examples 
# For set 1, the output should be 11; 1+4+6 at index 0,1,3, sum of the costs at these indices = 2+3+7 = 11 (which is <= 12)
# For set 2, the output should be 12; 3+4+5 at index 0,1,2, sum of the costs at these indices = 2+3+3 = 8 (which is <= 10)
