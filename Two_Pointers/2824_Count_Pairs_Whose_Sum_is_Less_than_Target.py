"""
LeetCode 2824. Count Pairs Whose Sum is Less than Target

Difficulty: Easy

Time Complexity: O(n log n)
Space Complexity: O(1)

Approach:
- Sort the array.
- Use two pointers:
  - left starts at the beginning.
  - right starts at the end.
- If nums[left] + nums[right] < target, then every element
  between left and right forms a valid pair with nums[left].
  Count all of them using (right - left) and move left forward.
- Otherwise, move right backward to reduce the sum.

This avoids checking every pair individually and improves the
time complexity over the brute-force O(n²) approach.
"""

from typing import List


class Solution:
    def countPairs(self, nums: List[int], target: int) -> int:
        nums.sort()

        left = 0
        right = len(nums) - 1
        count = 0

        while left < right:
            if nums[left] + nums[right] < target:
                count += right - left
                left += 1
            else:
                right -= 1

        return count
