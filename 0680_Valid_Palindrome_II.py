"""
LeetCode 680. Valid Palindrome II

Problem:
Given a string s, return true if it can be a palindrome after deleting
at most one character.

Approach:
- Use two pointers from both ends of the string.
- If characters match, continue moving inward.
- On the first mismatch, check whether skipping either the left
  or the right character results in a palindrome.
- If either check succeeds, return True.

Time Complexity: O(n)
Space Complexity: O(1)
"""

class Solution:
    def validPalindrome(self, s: str) -> bool:

        def check(left: int, right: int) -> bool:
            while left < right:
                if s[left] != s[right]:
                    return False
                left += 1
                right -= 1
            return True

        left = 0
        right = len(s) - 1

        while left < right:
            if s[left] != s[right]:
                return check(left + 1, right) or check(left, right - 1)

            left += 1
            right -= 1

        return True
