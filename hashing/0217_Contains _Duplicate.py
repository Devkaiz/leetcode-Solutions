"""
LeetCode 217. Contains Duplicate

Difficulty: Easy

Time Complexity: O(n)
Space Complexity: O(n)

Approach:
Use a HashSet to keep track of the numbers seen so far.
If the current number already exists in the set, a duplicate is found,
so return True. Otherwise, add the number to the set.
"""

from typing import List


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        seen = set()

        for num in nums:
            if num in seen:
                return True

            seen.add(num)

        return False
