"""
LeetCode 409. Longest Palindrome

Approach:
- Count the frequency of each character.
- Use all even frequencies.
- Use one odd frequency completely as the center.
- For remaining odd frequencies, use (frequency - 1).

Time Complexity: O(n)
Space Complexity: O(k)
"""

class Solution:
    def longestPalindrome(self, s: str) -> int:
        freq = {}
        out = 0
        center_used = False

        for ch in s:
            freq[ch] = freq.get(ch, 0) + 1

        for value in freq.values():
            if value % 2 == 0:
                out += value
            else:
                if not center_used:
                    out += value
                    center_used = True
                else:
                    out += value - 1

        return out
