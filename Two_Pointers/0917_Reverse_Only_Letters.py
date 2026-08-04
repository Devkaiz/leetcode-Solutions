"""
LeetCode 917. Reverse Only Letters

Problem:
Reverse only the English letters in a string while keeping all
non-letter characters in their original positions.

Approach:
- Convert the string into a list.
- Use two pointers from both ends.
- Skip non-letter characters.
- Swap letters when both pointers point to alphabetic characters.
- Convert the list back to a string.

Time Complexity: O(n)
Space Complexity: O(n)
"""

class Solution:
    def reverseOnlyLetters(self, s: str) -> str:
        word = list(s)

        left = 0
        right = len(word) - 1

        while left < right:
            if word[left].isalpha() and word[right].isalpha():
                word[left], word[right] = word[right], word[left]
                left += 1
                right -= 1

            elif not word[left].isalpha():
                left += 1

            elif not word[right].isalpha():
                right -= 1

        return "".join(word)
