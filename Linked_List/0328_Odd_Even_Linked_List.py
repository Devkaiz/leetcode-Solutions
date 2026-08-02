"""
LeetCode 328. Odd Even Linked List

Problem:
Given the head of a singly linked list, group all nodes with odd
indices together followed by the nodes with even indices.
The relative order inside the odd and even groups should remain the same.

Approach:
- Maintain two pointers for odd and even indexed nodes.
- Keep a reference to the head of the even list.
- Rearrange pointers to separate odd and even nodes.
- Connect the end of the odd list to the head of the even list.

Time Complexity: O(n)
Space Complexity: O(1)
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head

        odd = head
        even = head.next
        evenHead = even

        while even and even.next:
            odd.next = even.next
            odd = odd.next

            even.next = odd.next
            even = even.next

        odd.next = evenHead

        return head
