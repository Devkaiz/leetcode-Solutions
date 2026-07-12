"""
LeetCode 219. Contains Duplicate II

Difficulty: Easy

Time Complexity: O(n)
Space Complexity: O(n)

Approach:
Use a HashMap (dictionary) to store the most recent index of each element.

- Traverse the array once.
- If the current element has been seen before, calculate the distance
  between the current index and the previous index.
- If the distance is less than or equal to k, return True.
- Otherwise, update the element's latest index.
- If no such pair exists, return False.
"""

from typing import List


class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        last_seen = {}

        for i in range(len(nums)):
            if nums[i] in last_seen:
                if i - last_seen[nums[i]] <= k:
                    return True

            last_seen[nums[i]] = i

        return False
