"""
LeetCode 451. Sort Characters By Frequency

Approach:
- Count character frequencies.
- Sort characters by decreasing frequency.
- Build the answer by repeating each character.

Time Complexity: O(n + k log k)
Space Complexity: O(k)
"""

class Solution:
    def frequencySort(self, s: str) -> str:
        freq = {}

        for ch in s:
            freq[ch] = freq.get(ch, 0) + 1

        sorted_freq = sorted(freq.items(), key=lambda x: x[1], reverse=True)

        out = ""

        for ch, count in sorted_freq:
            out += ch * count

        return out
