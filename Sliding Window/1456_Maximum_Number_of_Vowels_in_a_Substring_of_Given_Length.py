"""
LeetCode 1456. Maximum Number of Vowels in a Substring of Given Length

Difficulty: Easy

Time Complexity: O(n)
Space Complexity: O(1)

Approach:
Use the Fixed Sliding Window technique.

- Count the vowels in the first window of size k.
- Store the count as the current maximum.
- Slide the window one character at a time.
- If the incoming character is a vowel, increase the count.
- If the outgoing character is a vowel, decrease the count.
- Update the maximum vowel count after each slide.

This avoids recalculating the vowel count for every substring, achieving O(n) time complexity.
"""

from typing import List


class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = {'a', 'e', 'i', 'o', 'u'}

        count = 0

        # Count vowels in the first window
        for i in range(k):
            if s[i] in vowels:
                count += 1

        max_count = count

        # Slide the window
        for right in range(k, len(s)):
            if s[right] in vowels:
                count += 1

            if s[right - k] in vowels:
                count -= 1

            max_count = max(max_count, count)

        return max_count
