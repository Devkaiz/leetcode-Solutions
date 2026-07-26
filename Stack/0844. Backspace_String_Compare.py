"""
LeetCode 844. Backspace String Compare

Problem:
Given two strings s and t containing lowercase letters and '#',
return True if they are equal after processing all backspaces.

Approach:
- Use two stacks to simulate typing.
- Push normal characters onto the stack.
- If a '#' is encountered, remove the previous character if possible.
- Compare the final stacks.

Time Complexity: O(n + m)
Space Complexity: O(n + m)

where:
n = length of s
m = length of t
"""

class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        stack1 = []
        stack2 = []

        for ch in s:
            if ch == "#":
                if stack1:
                    stack1.pop()
            else:
                stack1.append(ch)

        for ch in t:
            if ch == "#":
                if stack2:
                    stack2.pop()
            else:
                stack2.append(ch)

        return stack1 == stack2
