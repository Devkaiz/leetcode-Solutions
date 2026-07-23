"""
LeetCode 242. Valid Anagram

Difficulty: Easy

Time Complexity: O(n)
Space Complexity: O(n)

Approach:
Use two frequency dictionaries to count the occurrences of each character
in both strings. If the frequency dictionaries are identical, the strings
are anagrams; otherwise, they are not.
"""

from typing import List


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        freq1 = {}
        for char in s:
            if char in freq1:
                freq1[char] += 1
            else:
                freq1[char] = 1

        freq2 = {}
        for char in t:
            if char in freq2:
                freq2[char] += 1
            else:
                freq2[char] = 1

        return freq1 == freq2
