"""
LeetCode 876. Middle of the Linked List

Approach:
- Use two pointers:
  - slow moves one step at a time.
  - fast moves two steps at a time.
- When fast reaches the end, slow will be at the middle.

Time Complexity: O(n)
Space Complexity: O(1)
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow = head
        fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        return slow
