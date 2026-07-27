"""
LeetCode 1614. Maximum Nesting Depth of the Parentheses

Problem:
Given a valid parentheses string, return the maximum nesting depth
of the parentheses.

Approach:
- Traverse the string once.
- Increase the current depth for every '('.
- Decrease the current depth for every ')'.
- Keep track of the maximum depth encountered.

Time Complexity: O(n)
Space Complexity: O(1)
"""


class Solution:
    def maxDepth(self, s: str) -> int:
        max_depth = 0
        current_depth = 0

        for ch in s:
            if ch == "(":
                current_depth += 1
            elif ch == ")":
                current_depth -= 1

            max_depth = max(max_depth, current_depth)

        return max_depth
