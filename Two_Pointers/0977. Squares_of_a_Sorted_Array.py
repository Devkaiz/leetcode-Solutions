"""
LeetCode 977. Squares of a Sorted Array

Difficulty: Easy

Time Complexity: O(n)
Space Complexity: O(n)

Approach:
Use the Two Pointers technique.

The array is already sorted, but squaring negative numbers changes their order.
The largest square will always come from either the leftmost or rightmost element.

- Compare the squares of both ends.
- Place the larger square at the end of the answer array.
- Move the corresponding pointer.
- Continue until all elements are processed.

Return the sorted squared array.
"""

from typing import List


class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        ans = [0] * len(nums)

        left = 0
        right = len(nums) - 1
        index = len(nums) - 1

        while left <= right:
            left_square = nums[left] ** 2
            right_square = nums[right] ** 2

            if left_square < right_square:
                ans[index] = right_square
                right -= 1
            else:
                ans[index] = left_square
                left += 1

            index -= 1

        return ans
