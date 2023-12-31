# This is where we have the function(s) for part A, Exhaustive Search Approach.  
from itertools import combinations

class Stock:
    def __init__(self, numberOfStocks, cost):
        self.numberOfStocks = numberOfStocks
        self.cost = cost

def readStockDataFromFile(input):
    allStocks = []
    maxAmounts = []

    with open(input, 'r') as file:
        while True:
            line = file.readline()
            if not line.strip():
                break

            stockData = eval(file.readline().strip())
            currentSetStocks = []

            for data in stockData:
                currentSetStocks.append(Stock(*data))

            allStocks.append(currentSetStocks) 
            maxAmounts.append(int(file.readline().strip()))
            file.readline()

    return allStocks, maxAmounts

def writeResultToOutputFile(result):
    try:
        with open("outputExhaustiveSearch.txt", "w") as outputFile:
            outputFile.write(result + "\n") 
    except Exception as e:
        print(f"An error occurred: {str(e)}")

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


allStocks, maxAmounts = readStockDataFromFile('inputExhaustiveSearch.txt')
totalResults = ""

for setIndex, stocks in enumerate(allStocks):
    example = stockOptimization(maxAmounts[setIndex], stocks)
    result = 0
    for stock in example:
        result += stock.numberOfStocks
    totalResults += str(result)
    totalResults += "\n"

writeResultToOutputFile(totalResults)