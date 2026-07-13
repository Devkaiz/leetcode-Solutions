"""
LeetCode 209. Minimum Size Subarray Sum

Difficulty: Medium

Time Complexity: O(n)
Space Complexity: O(1)

Approach:
Use the Variable Sliding Window technique.

- Maintain a window using two pointers.
- Expand the window by moving the right pointer and adding elements to the current sum.
- Once the current sum becomes greater than or equal to the target, try shrinking the window from the left while maintaining the condition.
- Update the minimum window length during each valid window.
- If no valid subarray exists, return 0.

This approach processes each element at most twice, resulting in O(n) time complexity.
"""

from typing import List


class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left = 0
        window_sum = 0
        min_length = float("inf")

        for right in range(len(nums)):
            window_sum += nums[right]

            while window_sum >= target:
                min_length = min(min_length, right - left + 1)
                window_sum -= nums[left]
                left += 1

        if min_length == float("inf"):
            return 0

        return min_length
