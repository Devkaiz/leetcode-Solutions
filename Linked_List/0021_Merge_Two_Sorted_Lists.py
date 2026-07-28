"""
LeetCode 21. Merge Two Sorted Lists

Problem:
Merge two sorted linked lists and return the merged list.
The merged list should be made by splicing together the nodes
of the first two lists.

Approach:
- Create a dummy node to act as the starting point of the merged list.
- Maintain a pointer (curr) to the last node of the merged list.
- Compare the current nodes of both lists.
- Attach the smaller node to the merged list and move the corresponding pointer.
- After one list is exhausted, attach the remaining nodes of the other list.

Time Complexity: O(n + m)
Space Complexity: O(1)

where:
n = length of list1
m = length of list2
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def mergeTwoLists(
        self,
        list1: Optional[ListNode],
        list2: Optional[ListNode]
    ) -> Optional[ListNode]:

        dummy = ListNode()
        curr = dummy

        while list1 and list2:
            if list1.val < list2.val:
                curr.next = list1
                list1 = list1.next
            else:
                curr.next = list2
                list2 = list2.next

            curr = curr.next

        if list1:
            curr.next = list1
        else:
            curr.next = list2

        return dummy.next
