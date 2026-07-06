"""
LeetCode 344. Reverse String

Difficulty: Easy

Time Complexity: O(n)
Space Complexity: O(1)

Approach:
Use two pointers, one at the beginning and one at the end of the character
array. Swap the characters at both pointers and move them toward each other
until the pointers meet.
"""

from typing import List


class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        left = 0
        right = len(s) - 1

        while left < right:
            s[left], s[right] = s[right], s[left]
            left += 1
            right -= 1
