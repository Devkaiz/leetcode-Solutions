"""
LeetCode 121. Best Time to Buy and Sell Stock

Difficulty: Easy

Time Complexity: O(n)
Space Complexity: O(1)

Approach:
Traverse the prices array once while keeping track of the minimum price
seen so far. For each price, calculate the profit if the stock were sold
today and update the maximum profit accordingly.
"""

from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        min_index = 0
        max_profit = 0

        for i in range(n):
            if prices[i] < prices[min_index]:
                min_index = i

            curr_profit = prices[i] - prices[min_index]

            if curr_profit > max_profit:
                max_profit = curr_profit

        return max_profit
