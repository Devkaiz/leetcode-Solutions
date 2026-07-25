"""
LeetCode 496. Next Greater Element I

Problem:
Given two integer arrays nums1 and nums2, where nums1 is a subset of nums2,
return an array such that each element in nums1 is replaced by its next greater
element in nums2. If no greater element exists, return -1.

Approach:
- Use a monotonic decreasing stack while traversing nums2.
- Whenever the current number is greater than the top of the stack,
  pop the stack and store the mapping:
      smaller_number -> next_greater_number
- After processing nums2, use the hash map to build the answer for nums1.

Time Complexity: O(n + m)
Space Complexity: O(n)

where:
n = len(nums2)
m = len(nums1)
"""

from typing import List


class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stack = []
        next_greater = {}
        ans = []

        for num in nums2:
            while stack and stack[-1] < num:
                next_greater[stack.pop()] = num
            stack.append(num)

        for num in nums1:
            ans.append(next_greater.get(num, -1))

        return ans
