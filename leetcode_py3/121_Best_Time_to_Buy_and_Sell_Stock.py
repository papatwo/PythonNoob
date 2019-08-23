class Solution:
    def maxProfit(self, prices):
        if prices is None or len(prices) == 0:
            return 0
        min_price = prices[0]
        max_profit = 0
        
        for i in range(len(prices)):
            min_price = min(min_price, prices[i])

            max_profit = max(max_profit, prices[i]-min_price)

        return max_profit

if __name__ == '__main__':
    prices = [7,1,5,3,6,4]
    print(Solution().maxProfit(prices))


''' 
Say you have an array for which the ith element is the price of a given
stock on day i.

If you were only permitted to complete at most one transaction (i.e., buy one
and sell one share of the stock), design an algorithm to find the maximum
profit.

Note that you cannot sell a stock before you buy one.

Example 1:

Input: [7,1,5,3,6,4] Output: 5 Explanation: Buy on day 2 (price = 1) and sell
on day 5 (price = 6), profit = 6-1 = 5.              Not 7-1 = 6, as selling
price needs to be larger than buying price. Example 2:

Input: [7,6,4,3,1] Output: 0 Explanation: In this case, no transaction is
done, i.e. max profit = 0.
'''
