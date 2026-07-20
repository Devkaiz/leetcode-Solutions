from typing import List

class Solution:
    """
    LeetCode 49 - Group Anagrams

    Pattern:
    Hash Map + String Sorting

    Approach:
    - For each word, sort its characters to create a unique key.
    - Words that are anagrams produce the same sorted key.
    - Store the original words in a dictionary where:
        key   -> sorted word
        value -> list of anagrams
    - Return all grouped anagrams.

    Time Complexity:
        O(n × k log k)

    Space Complexity:
        O(n × k)
    """

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = {}

        for word in strs:
            key = "".join(sorted(word))

            if key in groups:
                groups[key].append(word)
            else:
                groups[key] = [word]

        return list(groups.values())
