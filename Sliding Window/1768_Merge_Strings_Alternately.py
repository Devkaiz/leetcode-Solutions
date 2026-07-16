"""
LeetCode 1768. Merge Strings Alternately

Difficulty: Easy

Time Complexity: O(n + m)
Space Complexity: O(n + m)

Approach:
Use the Two Pointers technique.

- Traverse both strings simultaneously until the shorter string ends.
- Append one character from each string alternately.
- If one string is longer, append its remaining characters.
- Return the merged string.

This efficiently merges both strings while preserving their order.
"""

class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        result = ""
        limit = min(len(word1), len(word2))

        for i in range(limit):
            result += word1[i] + word2[i]

        if len(word1) > len(word2):
            result += word1[len(word2):]
        elif len(word2) > len(word1):
            result += word2[len(word1):]

        return result
