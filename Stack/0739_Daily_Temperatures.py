"""
LeetCode 739. Daily Temperatures

Problem:
Given an array of daily temperatures, return an array such that
answer[i] is the number of days you have to wait after the ith day
to get a warmer temperature. If there is no future day, keep 0.

Approach:
- Use a monotonic decreasing stack to store (temperature, index).
- Traverse the array once.
- Whenever the current temperature is greater than the temperature
  at the top of the stack, pop it and calculate the waiting days.
- Push the current temperature and index onto the stack.

Time Complexity: O(n)
Space Complexity: O(n)
"""


class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        ans = [0] * len(temperatures)

        for i, t in enumerate(temperatures):
            while stack and t > stack[-1][0]:
                temp, index = stack.pop()
                ans[index] = i - index

            stack.append((t, i))

        return ans
