"""
LeetCode 160. Intersection of Two Linked Lists

Problem:
Given the heads of two singly linked lists, return the node at
which the two lists intersect. If the two linked lists have no
intersection, return None.

Approach:
- Use two pointers starting at the heads of both lists.
- Traverse each list.
- When a pointer reaches the end, redirect it to the head of the other list.
- If the lists intersect, both pointers will meet at the intersection node.
- If they do not intersect, both pointers will eventually become None.

Time Complexity: O(m + n)
Space Complexity: O(1)
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def getIntersectionNode(
        self,
        headA: ListNode,
        headB: ListNode
    ) -> Optional[ListNode]:

        a = headA
        b = headB

        while a != b:
            a = a.next if a else headB
            b = b.next if b else headA

        return a
