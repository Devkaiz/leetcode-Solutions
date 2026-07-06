"""
LeetCode 704. Binary Search

Difficulty: Easy

Time Complexity: O(log n)
Space Complexity: O(1)

Approach:
Use Binary Search on the sorted array. Compare the target with the middle
element. If the target is greater, search the right half. If it is smaller,
search the left half. Continue until the target is found or the search
space becomes empty.
"""

from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1

        while left <= right:
            middle = (left + right) // 2

            if nums[middle] < target:
                left = middle + 1

            elif nums[middle] > target:
                right = middle - 1

            else:
                return middle

        return -1
