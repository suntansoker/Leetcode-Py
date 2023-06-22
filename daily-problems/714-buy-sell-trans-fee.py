'''
You are given an array prices where prices[i] is the price of a given stock on the ith day, and an integer fee representing a transaction fee.

Find the maximum profit you can achieve. You may complete as many transactions as you like, but you need to pay the transaction fee for each transaction.

Note: You may not engage in multiple transactions simultaneously (i.e., you must sell the stock before you buy again).

 

Example 1:

Input: prices = [1,3,2,8,4,9], fee = 2
Output: 8
Explanation: The maximum profit can be achieved by:
- Buying at prices[0] = 1
- Selling at prices[3] = 8
- Buying at prices[4] = 4
- Selling at prices[5] = 9
The total profit is ((8 - 1) - 2) + ((9 - 4) - 2) = 8.
Example 2:

Input: prices = [1,3,7,5,10,3], fee = 3
Output: 6
 

Constraints:

1 <= prices.length <= 5 * 104
1 <= prices[i] < 5 * 104
0 <= fee < 5 * 104
'''


class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        n = len(prices)
        dp = [[-1 for _ in range(2)] for _ in range(n)]

        def findMaxProfit(index, buy):
            if index == n:
                return 0

            if dp[index][buy] != -1:
                return dp[index][buy]
            take, notTake = 0, 0
            if buy:
                take = findMaxProfit(index+1, 0) - prices[index]
                notTake = findMaxProfit(index+1, 1)
                res = max(take, notTake)
            else:
                take = findMaxProfit(index+1, 1) + prices[index] - fee
                notTake = findMaxProfit(index+1, 0)
                res = max(take, notTake)

            dp[index][buy] = res
            return dp[index][buy]

        return findMaxProfit(0, 1)
