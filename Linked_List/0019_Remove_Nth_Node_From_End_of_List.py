"""
LeetCode 19. Remove Nth Node From End of List

Problem:
Given the head of a linked list, remove the nth node from the end
of the list and return its head.

Approach:
- Create a dummy node pointing to the head.
- Use two pointers (fast and slow) starting at the dummy node.
- Move the fast pointer n + 1 steps ahead to maintain a gap.
- Move both pointers together until fast reaches the end.
- The slow pointer will be just before the node to remove.
- Skip the target node and return the updated list.

Time Complexity: O(n)
Space Complexity: O(1)
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def removeNthFromEnd(
        self,
        head: Optional[ListNode],
        n: int
    ) -> Optional[ListNode]:

        dummy = ListNode()
        dummy.next = head

        slow = fast = dummy

        for _ in range(n + 1):
            fast = fast.next

        while fast:
            fast = fast.next
            slow = slow.next

        slow.next = slow.next.next

        return dummy.next
