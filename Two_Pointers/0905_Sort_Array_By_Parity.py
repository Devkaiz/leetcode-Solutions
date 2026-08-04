"""
LeetCode 905. Sort Array By Parity

Problem:
Given an integer array nums, move all even integers to the beginning
of the array followed by all the odd integers.

Approach:
- Use two pointers starting from both ends.
- Move the left pointer until it finds an odd number.
- Move the right pointer until it finds an even number.
- Swap the misplaced elements.
- Continue until both pointers meet.

Time Complexity: O(n)
Space Complexity: O(1)
"""

class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        left = 0
        right = len(nums) - 1

        while left < right:
            if nums[left] % 2 == 0:
                left += 1
            elif nums[right] % 2 != 0:
                right -= 1
            else:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
                right -= 1

        return nums
