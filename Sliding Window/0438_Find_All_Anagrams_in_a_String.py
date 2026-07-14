"""
LeetCode 438. Find All Anagrams in a String

Difficulty: Medium

Time Complexity: O(n)
Space Complexity: O(1)

Approach:
Use a Fixed Sliding Window with a Frequency Map.

- Count the frequency of characters in the pattern string.
- Build a frequency map for the first window in the source string.
- Slide the window one character at a time by:
    - Adding the incoming character.
    - Removing the outgoing character.
- Whenever both frequency maps match, record the starting index.

Since the alphabet contains only lowercase English letters,
the frequency comparison is effectively constant time.
"""

from collections import Counter
from typing import List


class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:

        if len(p) > len(s):
            return []

        p_count = Counter(p)
        window = Counter(s[:len(p)])

        ans = []

        if window == p_count:
            ans.append(0)

        for right in range(len(p), len(s)):

            window[s[right]] += 1

            left_char = s[right - len(p)]
            window[left_char] -= 1

            if window[left_char] == 0:
                del window[left_char]

            if window == p_count:
                ans.append(right - len(p) + 1)

        return ans
