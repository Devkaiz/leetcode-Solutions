"""
LeetCode 1343. Number of Sub-arrays of Size K and Average Greater than or Equal to Threshold

Difficulty: Medium

Time Complexity: O(n)
Space Complexity: O(1)

Approach:
Use the Fixed Sliding Window technique.

- Compute the sum of the first window of size k.
- Check if its average is greater than or equal to the threshold.
- Slide the window by adding the incoming element and removing the outgoing element.
- Count every window whose average satisfies the condition.

This processes each element only once, achieving O(n) time complexity.
"""

from typing import List

class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        target = threshold * k

        window_sum = 0
        count = 0

        for i in range(k):
            window_sum += arr[i]

        if window_sum >= target:
            count += 1

        for right in range(k, len(arr)):
            window_sum += arr[right] - arr[right - k]

            if window_sum >= target:
                count += 1

        return count
