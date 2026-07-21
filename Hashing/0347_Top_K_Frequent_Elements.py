from typing import List

class Solution:
    """
    LeetCode 347 - Top K Frequent Elements

    Pattern:
    Hash Map + Sorting

    Approach:
    - Count the frequency of each element using a hash map.
    - Sort the dictionary items based on frequency in descending order.
    - Return the first k elements (keys).

    Time Complexity:
        O(n log n)

    Space Complexity:
        O(n)
    """

    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}

        for num in nums:
            freq[num] = freq.get(num, 0) + 1

        sorted_items = sorted(freq.items(), key=lambda x: x[1], reverse=True)

        return [key for key, _ in sorted_items[:k]]
