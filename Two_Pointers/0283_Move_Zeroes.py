"""
LeetCode 283. Move Zeroes

Difficulty: Easy

Time Complexity: O(n)
Space Complexity: O(1)

Approach:
Use the Two Pointers technique.

- The 'read' pointer traverses the array.
- The 'write' pointer keeps track of where the next non-zero element should be placed.

First, copy all non-zero elements to the front of the array.
After all non-zero elements are placed, fill the remaining positions with zeros.

The array is modified in-place as required.
"""

from typing import List


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        write = 0

        for read in range(len(nums)):
            if nums[read] != 0:
                nums[write] = nums[read]
                write += 1

        for i in range(write, len(nums)):
            nums[i] = 0
