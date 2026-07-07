"""
LeetCode 27. Remove Element

Difficulty: Easy

Time Complexity: O(n)
Space Complexity: O(1)

Approach:
Use two pointers. One pointer scans every element, while the other keeps
track of where the next valid element should be placed. Ignore elements
equal to val and overwrite the array with the remaining elements.
"""

from typing import List


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        write = 0

        for read in range(len(nums)):
            if nums[read] != val:
                nums[write] = nums[read]
                write += 1

        return write
