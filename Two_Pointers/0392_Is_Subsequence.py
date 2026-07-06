"""
LeetCode 392. Is Subsequence

Difficulty: Easy

Time Complexity: O(n)
Space Complexity: O(1)

Approach:
Use two pointers to traverse both strings. Move both pointers when the
characters match. Otherwise, move only the pointer in the second string.
If the first pointer reaches the end of the first string, then it is a
subsequence of the second string.
"""

class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        i = j = 0
        n = len(s)
        m = len(t)

        while i < n and j < m:
            if s[i] == t[j]:
                i += 1
                j += 1
            else:
                j += 1

        return i == n
