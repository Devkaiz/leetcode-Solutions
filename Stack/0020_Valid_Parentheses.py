"""
LeetCode 20. Valid Parentheses

Difficulty: Easy

Time Complexity: O(n)
Space Complexity: O(n)

Approach:
Use a stack to keep track of opening brackets.
- Push opening brackets onto the stack.
- For every closing bracket, check if it matches the top of the stack.
- If it matches, pop the opening bracket.
- If it doesn't match or the stack is empty, return False.
- At the end, the stack should be empty for the string to be valid.
"""

from typing import List


class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        for ch in s:
            if ch in "([{":
                stack.append(ch)

            elif not stack:
                return False

            elif ch == "]" and stack[-1] == "[":
                stack.pop()

            elif ch == "}" and stack[-1] == "{":
                stack.pop()

            elif ch == ")" and stack[-1] == "(":
                stack.pop()

            else:
                return False

        return len(stack) == 0
