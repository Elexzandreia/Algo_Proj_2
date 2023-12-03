#This is where we'll have the function(s) for the Dynamic Programming Approach, part B.
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

def writeResultToOutputFile(results):
    try:
        with open("outputDP.txt", "w") as outputFile:
            for result in results:
                outputFile.write(result + "\n")
    except Exception as e:
        print(f"An error occurred: {str(e)}")

def stockOptimization(maxAmountAllowed, stocks):
    stockLength = len(stocks)
    dp = [0] * (maxAmountAllowed+1)

    for i in range(1, stockLength+1):
        for j in range(maxAmountAllowed, 0, -1):
            for k in range(stocks[i-1].cost, j+1):
                dp[j] = max(dp[j], dp[j-k] + stocks[i-1].numberOfStocks)

    return dp[maxAmountAllowed]

allStocks, maxAmounts = readStockDataFromFile('inputDP.txt')
results = []

for setIndex, stocks in enumerate(allStocks):
    result = stockOptimization(maxAmounts[setIndex], stocks)
    results.append(str(result))

writeResultToOutputFile(results)
