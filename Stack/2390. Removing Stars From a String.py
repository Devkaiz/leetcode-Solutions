"""
LeetCode 2390. Removing Stars From a String

Problem:
Given a string containing letters and '*' characters,
remove each '*' along with the closest non-star character to its left.

Approach:
- Use a stack to store characters.
- If the current character is '*', remove the last character from the stack.
- Otherwise, push the character onto the stack.
- Join the remaining characters to form the final string.

Time Complexity: O(n)
Space Complexity: O(n)
"""

class Solution:
    def removeStars(self, s: str) -> str:
        stack = []

        for ch in s:
            if ch == "*":
                stack.pop()
            else:
                stack.append(ch)

        return "".join(stack)
