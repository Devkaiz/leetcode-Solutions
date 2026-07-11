"""
LeetCode 167. Two Sum II - Input Array Is Sorted

Difficulty: Medium

Time Complexity: O(n)
Space Complexity: O(1)

Approach:
Since the array is already sorted, use two pointers.

- Initialize one pointer at the beginning and another at the end.
- Calculate the sum of both elements.
- If the sum equals the target, return their 1-based indices.
- If the sum is smaller than the target, move the left pointer to increase the sum.
- If the sum is larger than the target, move the right pointer to decrease the sum.

This approach finds the answer in a single pass.
"""

from typing import List


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left = 0
        right = len(numbers) - 1

        while left < right:
            current = numbers[left] + numbers[right]

            if current < target:
                left += 1
            elif current > target:
                right -= 1
            else:
                return [left + 1, right + 1]
