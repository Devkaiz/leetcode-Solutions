"""
LeetCode 2656. Maximum Sum With Exactly K Elements

Difficulty: Easy

Time Complexity: O(n + k)
Space Complexity: O(1)

Approach:
Find the maximum element in the array.

- Select the maximum element and add it to the score.
- After each selection, the chosen element increases by one.
- Instead of modifying the array, observe that the selected values form the sequence:
  maximum, maximum + 1, maximum + 2, ...
- Sum these values for k selections.

This avoids unnecessary array updates and achieves an efficient solution.
"""

from typing import List


class Solution:
    def maximizeSum(self, nums: List[int], k: int) -> int:
        maximum = max(nums)
        score = 0

        for i in range(k):
            score += maximum + i

        return score
