"""
LeetCode 1290. Convert Binary Number in a Linked List to Integer

Problem:
Given the head of a singly linked list where each node contains
either 0 or 1, return the decimal value of the binary number.

Approach:
- Traverse the linked list from left to right.
- Multiply the current result by 2 (left shift).
- Add the current node's value.

Time Complexity: O(n)
Space Complexity: O(1)
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        result = 0

        while head:
            result = result * 2 + head.val
            head = head.next

        return result
