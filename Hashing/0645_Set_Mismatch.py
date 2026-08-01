"""
LeetCode 645. Set Mismatch

Problem:
You are given an array representing a set of numbers from 1 to n,
where one number appears twice and one number is missing.
Return the duplicate number and the missing number.

Approach:
- Create an empty set to store visited numbers.
- Traverse the array to identify the duplicate element.
- Iterate from 1 to n.
- The number that is not present in the set is the missing number.
- Return the duplicate and missing numbers as a list.

Time Complexity: O(n)
Space Complexity: O(n)
"""

class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        s = set()
        n = len(nums)

        for i in nums:
            if i not in s:
                s.add(i)
            else:
                duplicate = i

        for j in range(1, n + 1):
            if j not in s:
                missing = j

        return [duplicate, missing]
