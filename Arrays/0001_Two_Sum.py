"""
LeetCode 1. Two Sum
Difficulty: Easy

Time Complexity: O(n)
Space Complexity: O(n)

Approach:
Use a hash map to store previously seen numbers and their indices.
For each number, check whether its complement (target - number)
already exists in the hash map.
"""

from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prev = {}  # Store number -> index

        for i, n in enumerate(nums):
            diff = target - n

            if diff in prev:
                return [prev[diff], i]

            prev[n] = i
