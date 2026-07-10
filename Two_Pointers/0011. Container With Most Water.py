"""
LeetCode 11. Container With Most Water

Difficulty: Medium

Time Complexity: O(n)
Space Complexity: O(1)

Approach:
Use the Two Pointers technique.

- Initialize one pointer at the beginning and another at the end of the array.
- The area is determined by:
    Area = min(left_height, right_height) × width
- Update the maximum area found.
- Move the pointer pointing to the shorter line, since moving the taller line cannot increase the area.
- Continue until both pointers meet.

Return the maximum area.
"""

from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        left = 0
        right = len(height) - 1
        max_area = 0

        while left < right:
            area = min(height[left], height[right]) * (right - left)
            max_area = max(max_area, area)

            if height[left] > height[right]:
                right -= 1
            else:
                left += 1

        return max_area
