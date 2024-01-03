# Input: prices = [7,1,5,3,6,4]
# Output: 5
# Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
# Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.


def maxProfit(prices):
    if len(prices) < 2:
        return 0
    profits = []
    maxProfit = 0 
    minProfit = prices[0]
    
    for i in range(0, len(prices)):
        minProfit = min(minProfit, prices[i])
        maxProfit = max(maxProfit, prices[i] - minProfit)
    print(maxProfit)
    return maxProfit

maxProfit([7,1,5,3,6,4])
