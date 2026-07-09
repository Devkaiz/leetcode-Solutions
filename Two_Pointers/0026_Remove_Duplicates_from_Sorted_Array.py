"""
LeetCode 26. Remove Duplicates from Sorted Array

Difficulty: Easy

Time Complexity: O(n)
Space Complexity: O(1)

Approach:
Since the array is already sorted, duplicate elements appear next to each other.
Use two pointers:
- 'read' traverses the array.
- 'write' keeps track of the next position for a unique element.

Whenever a new unique element is found, copy it to the 'write' position
and move the write pointer forward.

Return the number of unique elements.
"""

from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0

        write = 1

        for read in range(1, len(nums)):
            if nums[read] != nums[read - 1]:
                nums[write] = nums[read]
                write += 1

        return write
