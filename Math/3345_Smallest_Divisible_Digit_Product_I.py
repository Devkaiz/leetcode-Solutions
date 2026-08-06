"""
LeetCode 3345. Smallest Divisible Digit Product I

Problem:
Given two integers n and t, find the smallest integer greater than or
equal to n whose product of digits is divisible by t.

Approach:
- Check each number starting from n.
- Compute the product of its digits.
- If the digit product is divisible by t, return the number.
- The problem guarantees that the answer exists within the next 10 numbers.

Time Complexity: O(1)
Space Complexity: O(1)
"""

class Solution:
    def smallestNumber(self, n: int, t: int) -> int:
        for i in range(n, n + 11):
            product = 1

            for digit in str(i):
                product *= int(digit)

            if product % t == 0:
                return i
