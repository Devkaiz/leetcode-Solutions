"""
LeetCode 206. Reverse Linked List

Problem:
Given the head of a singly linked list, reverse the list
and return the new head.

Approach:
- Maintain two pointers:
    1. prev - points to the reversed part of the list.
    2. curr - points to the current node being processed.
- Save the next node before changing pointers.
- Reverse the current node's link.
- Move both pointers one step forward.
- Repeat until the end of the list.

Time Complexity: O(n)
Space Complexity: O(1)
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        curr = head

        while curr:
            nex = curr.next
            curr.next = prev
            prev = curr
            curr = nex

        return prev
