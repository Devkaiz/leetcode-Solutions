"""
LeetCode 143. Reorder List

Problem:
Given the head of a singly linked list, reorder the list as:
L0 → Ln → L1 → Ln-1 → L2 → Ln-2 → ...

The reordering must be done in-place without modifying node values.

Approach:
- Find the middle of the linked list using fast and slow pointers.
- Split the list into two halves.
- Reverse the second half.
- Merge the two halves by alternating nodes.

Time Complexity: O(n)
Space Complexity: O(1)
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """

        if not head or not head.next:
            return

        # Find the middle of the list
        slow = fast = head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next

        # Split the list
        second = slow.next
        slow.next = None

        # Reverse the second half
        prev = None
        curr = second
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt

        # Merge the two halves
        left = head
        right = prev

        while right:
            nextLeft = left.next
            nextRight = right.next

            left.next = right
            right.next = nextLeft

            left = nextLeft
            right = nextRight
