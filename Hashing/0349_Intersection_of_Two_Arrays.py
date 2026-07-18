"""
LeetCode 349. Intersection of Two Arrays

Difficulty: Easy

Time Complexity: O(n + m)
Space Complexity: O(m)

Approach:
- Convert the second array into a hash set for fast lookups.
- Traverse the first array.
- If an element exists in the hash set and hasn't already been added
  to the result, include it.
- Return the list of unique common elements.

Using a hash set reduces membership checking from O(n) to O(1) on average.
"""

from typing import List


class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        out = []
        nums2_set = set(nums2)

        for num in nums1:
            if num in nums2_set and num not in out:
                out.append(num)

        return out
