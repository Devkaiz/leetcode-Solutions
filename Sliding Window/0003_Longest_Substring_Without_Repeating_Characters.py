"""
LeetCode 3. Longest Substring Without Repeating Characters

Difficulty: Medium

Time Complexity: O(n)
Space Complexity: O(n)

Approach:
Use the Sliding Window technique with a HashSet.

- Maintain a window using two pointers (left and right).
- Expand the window by moving the right pointer.
- If a duplicate character is found, keep shrinking the window
  from the left until the duplicate is removed.
- Track the maximum window size throughout the traversal.

This ensures every character is processed at most twice,
resulting in O(n) time complexity.
"""

from typing import List


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = set()
        left = 0
        max_length = 0

        for right in range(len(s)):
            while s[right] in seen:
                seen.remove(s[left])
                left += 1

            seen.add(s[right])
            max_length = max(max_length, right - left + 1)

        return max_length
