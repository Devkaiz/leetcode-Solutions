"""
LeetCode 83. Remove Duplicates from Sorted List

Problem:
Given the head of a sorted linked list, delete all duplicates
such that each element appears only once.
Return the linked list sorted as well.

Approach:
- Traverse the linked list using a single pointer.
- Compare the current node with the next node.
- If both values are equal, skip the duplicate node.
- Otherwise, move to the next node.
- Return the modified head.

Time Complexity: O(n)
Space Complexity: O(1)
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr = head

        while curr and curr.next:
            if curr.val == curr.next.val:
                curr.next = curr.next.next
            else:
                curr = curr.next

        return head
