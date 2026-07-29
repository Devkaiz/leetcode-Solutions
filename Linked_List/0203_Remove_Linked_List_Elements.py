"""
LeetCode 203. Remove Linked List Elements

Problem:
Given the head of a linked list and an integer val,
remove all the nodes of the linked list that have Node.val == val,
and return the new head.

Approach:
- Create a dummy node pointing to the head.
- Traverse the list using a pointer starting from the dummy node.
- If the next node contains the target value, skip it.
- Otherwise, move to the next node.
- Return the updated list starting from dummy.next.

Time Complexity: O(n)
Space Complexity: O(1)
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        dummy = ListNode()
        dummy.next = head

        curr = dummy

        while curr.next:
            if curr.next.val == val:
                curr.next = curr.next.next
            else:
                curr = curr.next

        return dummy.next
