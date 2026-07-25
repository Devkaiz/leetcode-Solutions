"""
LeetCode 682. Baseball Game

Problem:
You are given a list of operations representing a baseball game's score record.
Return the sum of all valid scores after performing all the operations.

Operations:
- Integer: Record a new score.
- "+": Record a score that is the sum of the previous two scores.
- "D": Record a score that is double the previous score.
- "C": Remove the previous score.

Approach:
- Use a stack to store valid scores.
- Perform each operation based on its type.
- Return the sum of the stack after processing all operations.

Time Complexity: O(n)
Space Complexity: O(n)
"""

from typing import List


class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []

        for op in operations:
            if op == "C":
                stack.pop()
            elif op == "D":
                stack.append(2 * stack[-1])
            elif op == "+":
                stack.append(stack[-1] + stack[-2])
            else:
                stack.append(int(op))

        return sum(stack)
