# This is where we'll have the function(s) for part A, Exhaustive Search Approach.  
from itertools import combinations

class Stock:
    def __init__(self, numberOfStocks, cost):
        self.numberOfStocks = numberOfStocks
        self.cost = cost

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

# Examples 
stocks = [Stock(1, 2), Stock(4, 3), Stock(3, 6), Stock(6, 7)]
maxCostAmount = 12
#output should be 11; 1+4+6 at index 0,1,3, sum of the costs at these indices = 2+3+7<=12
example1 = stockOptimization(maxCostAmount, stocks)
result1 = 0
print("First example:")
for stock in example1:
    result1 += stock.numberOfStocks
print(result1)

stocks2 = [Stock(3, 2), Stock(4, 3), Stock(5, 3), Stock(6, 7)]
maxCostAmount2 = 10
# output should be 12; 3+4+5 at index 0,1,2, sum of the costs at these indices = 2+3+3<=10
example2 = stockOptimization(maxCostAmount2, stocks2)
result2 = 0
print("Second example:")
for stock in example2:
    result2 += stock.numberOfStocks
print(result2)


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

# Read stocks and max amounts from file
allStocks, maxAmounts = readStockDataFromFile('input.txt')

# Example to show the read stocks and max amounts
for setIndex, stocks in enumerate(allStocks):
    print(f"Set {setIndex + 1}:")
    for stock in stocks:
        print(f"  Number of Stocks: {stock.numberOfStocks}, Cost: {stock.cost}")
    print(f"Max Amount for Set {setIndex + 1}: {maxAmounts[setIndex]}")
    print()
