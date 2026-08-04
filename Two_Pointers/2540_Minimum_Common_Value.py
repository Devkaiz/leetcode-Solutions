"""
LeetCode 2540. Minimum Common Value

Problem:
Given two sorted integer arrays, return the minimum common value.
If there is no common value, return -1.

Approach:
- Use two pointers, one for each sorted array.
- Compare the current elements.
- Move the pointer pointing to the smaller element.
- If both elements are equal, return the value.
- If no common element exists, return -1.

Time Complexity: O(m + n)
Space Complexity: O(1)
"""

class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        i = 0
        j = 0

        while i < len(nums1) and j < len(nums2):
            if nums1[i] == nums2[j]:
                return nums1[i]
            elif nums1[i] < nums2[j]:
                i += 1
            else:
                j += 1

        return -1
