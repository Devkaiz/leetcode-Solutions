"""
LeetCode 1047. Remove All Adjacent Duplicates In String

Problem:
Given a string, repeatedly remove adjacent duplicate characters
until no adjacent duplicates remain.

Approach:
- Use a stack to keep track of characters.
- If the current character matches the top of the stack,
  remove the top character.
- Otherwise, push the current character onto the stack.
- Join the remaining characters to form the final string.

Time Complexity: O(n)
Space Complexity: O(n)
"""


class Solution:
    def removeDuplicates(self, s: str) -> str:
        stack = []

        for ch in s:
            if stack and stack[-1] == ch:
                stack.pop()
            else:
                stack.append(ch)

        return "".join(stack)
