# El's got this part/file...

# This is where we'll have the function(s) for part A, Exhaustive Search Approach.  
# Right now, it's optimizing the "numberOfStocks" & keeping that under the "maxCostAmount", when it SHOULD be optimizing the "cost" and keeping THAT under "maxCostAmount"
# Then the output (of everything @ the end) should be the item.numberOfStocks total of the cadidateItems 

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
                if currentBest is None or totalCost(candidateStocks) > totalCost(currentBest):
                    currentBest = candidateStocks
    return currentBest

def verifyCandidateStocks(maxAmountAllowed, candidateStocks):
    totalNumberOfStocks = sum(stock.numberOfStocks for stock in candidateStocks) # i believe i need to change "sum(stock.numberOfStocks" to "sum(stock.cost" bc that would mean its valid... 
    if totalNumberOfStocks <= maxAmountAllowed: # & also change "totalNumberOfStocks" to "totalCost"
        return True
    else:
        return False

def totalCost(candidateStocks):
    totalCost = sum(stock.cost for stock in candidateStocks)
    return totalCost

# Examples 
stocks = [Stock(1, 2), Stock(4, 3), Stock(3, 6), Stock(6, 7)]
maxCostAmount = 12
#output should be 11; 1+4+6 at index 0,1,3, sum of the costs at these indices = 2+3+7<=12
result = stockOptimization(maxCostAmount, stocks)
print("First example:")
for stock in result:
    print("({}, {})".format(stock.numberOfStocks, stock.cost))

stocks2 = [Stock(3, 2), Stock(4, 3), Stock(5, 3), Stock(6, 7)]
maxCostAmount2 = 10
# output should be 12; 3+4+5 at index 0,1,2, sum of the costs at these indices = 2+3+3<=10
result2 = stockOptimization(maxCostAmount2, stocks2)
print("Second example:")
for stock2 in result2:
    print("({}, {})".format(stock2.numberOfStocks, stock2.cost))


#__________________PSEUDOCODE_FROM_KNAPSACK_LECTURE____________________
# def stock_optimization(W, items):
#   currentBest = None
#   for candidate_items in subsets(items):
#       if verifyCandidateStocks(W, items, candidate_items):
#           if currentBest is None or total_cost(candidate_items) > total_cost(currentBest)
#               currentBest = candidate
#   return currentBest

# def verifyCandidateStocks(W, items, candidate_items):
#   total_numberOfStocks = 0
#   for item in candidate_items:
#       total_numberOfStocks += item.numberOfStocks
#   if total_numberOfStocks <= W:
#       return True
#   else:
#       return False

# def total_cost(candidate_items):
#   total_cost = 0
#   for item in candidate_items:
#       total_cost += item.cost
#   return total_cost

# "The exhaustive search algorithm for the knapsack problem runs in O(2^n * n) time"
