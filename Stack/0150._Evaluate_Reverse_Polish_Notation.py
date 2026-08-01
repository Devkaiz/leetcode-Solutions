"""
LeetCode 150. Evaluate Reverse Polish Notation

Problem:
Evaluate the value of an arithmetic expression written in Reverse
Polish Notation (RPN).

Approach:
- Use a stack to store operands.
- Traverse each token in the expression.
- If the token is a number, push it onto the stack.
- If the token is an operator, pop the top two operands,
  perform the operation, and push the result back.
- The final value remaining in the stack is the answer.

Time Complexity: O(n)
Space Complexity: O(n)
"""

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        nums = []
        res = 0

        for i in tokens:
            if i == "+":
                res = nums[-2] + nums[-1]
                nums.pop()
                nums.pop()
                nums.append(res)

            elif i == "-":
                res = nums[-2] - nums[-1]
                nums.pop()
                nums.pop()
                nums.append(res)

            elif i == "/":
                res = nums[-2] / nums[-1]
                nums.pop()
                nums.pop()
                nums.append(int(res))

            elif i == "*":
                res = nums[-2] * nums[-1]
                nums.pop()
                nums.pop()
                nums.append(res)

            else:
                nums.append(int(i))

        return nums[0]
