"""
LeetCode 205. Isomorphic Strings

Difficulty: Easy

Time Complexity: O(n)
Space Complexity: O(n)

Approach:
- Use two hash maps to maintain a one-to-one mapping between
  characters in both strings.
- The first map stores the mapping from s to t.
- The second map stores the reverse mapping from t to s.
- While traversing both strings simultaneously, verify that
  existing mappings remain consistent. If any mismatch occurs,
  return False.
- If all mappings are valid, return True.

This ensures that no two different characters map to the same
character and every mapping is unique.
"""

from typing import Dict


class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        s_t = {}
        t_s = {}

        for a, b in zip(s, t):
            if a not in s_t:
                s_t[a] = b
            elif s_t[a] != b:
                return False

            if b not in t_s:
                t_s[b] = a
            elif t_s[b] != a:
                return False

        return True
