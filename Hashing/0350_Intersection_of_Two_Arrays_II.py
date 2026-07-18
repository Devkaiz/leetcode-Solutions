"""
LeetCode 350. Intersection of Two Arrays II

Difficulty: Easy

Time Complexity: O(n + m)
Space Complexity: O(n)

Approach:
- Store the frequency of each element in nums1 using a hash map.
- Traverse nums2.
- If the current element exists in the hash map with a positive count:
    - Add it to the result.
    - Decrease its frequency by 1.
- Return the resulting list.

This ensures that each element appears in the output the minimum number of
times it appears in both arrays.
"""

from typing import List


class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        freq = {}
        result = []

        for num in nums1:
            freq[num] = freq.get(num, 0) + 1

        for num in nums2:
            if num in freq and freq[num] > 0:
                result.append(num)
                freq[num] -= 1

        return result
