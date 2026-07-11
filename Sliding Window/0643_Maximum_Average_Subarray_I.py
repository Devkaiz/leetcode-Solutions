"""
LeetCode 643. Maximum Average Subarray I

Difficulty: Easy

Time Complexity: O(n)
Space Complexity: O(1)

Approach:
Use the Sliding Window technique.

- Compute the sum of the first window of size k.
- Store its average as the current maximum average.
- Slide the window one element at a time by:
    - Adding the incoming element.
    - Removing the outgoing element.
- Update the maximum average after each slide.
- Return the highest average found.

This avoids recalculating the sum for every subarray, reducing the time complexity from O(n*k) to O(n).
"""

from typing import List


class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        window_sum = 0

        for i in range(k):
            window_sum += nums[i]

        max_avg = window_sum / k

        for i in range(k, len(nums)):
            window_sum = window_sum + nums[i] - nums[i - k]
            max_avg = max(max_avg, window_sum / k)

        return max_avg
