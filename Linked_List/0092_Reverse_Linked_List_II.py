"""
LeetCode 92. Reverse Linked List II

Problem:
Given the head of a singly linked list and two integers left and right,
reverse the nodes from position left to right and return the modified list.

Approach:
- Create a dummy node to simplify edge cases.
- Traverse to the node just before the left position.
- Reverse exactly (right - left + 1) nodes using the standard linked list reversal algorithm.
- Reconnect the reversed sublist with the remaining parts of the linked list.

Time Complexity: O(n)
Space Complexity: O(1)
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:

        if not head or left == right:
            return head

        dummy = ListNode(0, head)
        before = dummy

        # Move to the node before the left position
        for _ in range(left - 1):
            before = before.next

        first = before.next
        prev = None
        curr = first

        # Reverse the sublist
        for _ in range(right - left + 1):
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt

        # Reconnect the reversed sublist
        before.next = prev
        first.next = curr

        return dummy.next
