"""
LeetCode 234. Palindrome Linked List

Problem:
Given the head of a singly linked list, return true if it is
a palindrome, otherwise return false.

Approach:
- Use fast and slow pointers to find the middle of the list.
- Reverse the second half of the linked list.
- Compare the first half with the reversed second half.
- If all corresponding values match, the linked list is a palindrome.

Time Complexity: O(n)
Space Complexity: O(1)
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        slow = head
        fast = head.next

        # Find the middle of the linked list
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # Reverse the second half
        prev = None
        curr = slow.next

        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp

        # Compare both halves
        while prev:
            if head.val != prev.val:
                return False
            head = head.next
            prev = prev.next

        return True
