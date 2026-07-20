from typing import List

class Solution:
    """
    LeetCode 567 - Permutation in String

    Pattern:
    Sliding Window + Hash Map (Frequency Count)

    Approach:
    - Build frequency maps for s1 and the first window of s2.
    - Compare the maps.
    - Slide the window one character at a time:
        * Add the incoming character.
        * Remove the outgoing character.
        * Delete the key if its count becomes zero.
    - If the maps match at any point, return True.
    - Otherwise, return False.

    Time Complexity:
        O(n)

    Space Complexity:
        O(1)
    """

    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s2) < len(s1):
            return False

        s1map = {}
        s2map = {}

        for i in range(len(s1)):
            s1map[s1[i]] = s1map.get(s1[i], 0) + 1
            s2map[s2[i]] = s2map.get(s2[i], 0) + 1

        if s1map == s2map:
            return True

        left = 0

        for right in range(len(s1), len(s2)):
            s2map[s2[right]] = s2map.get(s2[right], 0) + 1

            s2map[s2[left]] -= 1
            if s2map[s2[left]] == 0:
                del s2map[s2[left]]

            left += 1

            if s1map == s2map:
                return True

        return False
