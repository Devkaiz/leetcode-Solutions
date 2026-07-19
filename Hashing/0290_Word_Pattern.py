"""
LeetCode 290. Word Pattern

Difficulty: Easy

Time Complexity: O(n)
Space Complexity: O(n)

Approach:
- Split the input string into a list of words.
- If the number of words does not match the pattern length,
  return False.
- Use two hash maps:
    - pattern_to_word maps each pattern character to a word.
    - word_to_pattern maps each word back to a pattern character.
- While traversing both simultaneously, verify that existing
  mappings remain consistent.
- If any mapping conflicts, return False.
- Otherwise, establish new mappings and continue.
- Return True if all mappings are valid.

This ensures a one-to-one correspondence between pattern
characters and words.
"""

from typing import Dict


class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        words = s.split()

        if len(pattern) != len(words):
            return False

        pattern_to_word = {}
        word_to_pattern = {}

        for p, w in zip(pattern, words):
            if p in pattern_to_word and pattern_to_word[p] != w:
                return False
            if w in word_to_pattern and word_to_pattern[w] != p:
                return False

            pattern_to_word[p] = w
            word_to_pattern[w] = p

        return True
