"""
LeetCode 2379. Minimum Recolors to Get K Consecutive Black Blocks

Difficulty: Easy

Time Complexity: O(n)
Space Complexity: O(1)

Approach:
Use the Fixed Sliding Window technique.

- Count the number of white blocks ('W') in the first window of size k.
- Store this as the current minimum recolors needed.
- Slide the window by adding the incoming block and removing the outgoing block.
- Update the minimum number of recolors required after each slide.

This efficiently finds the answer in O(n) time.
"""

class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        count = 0

        for i in range(k):
            if blocks[i] == "W":
                count += 1

        minimum = count

        for right in range(k, len(blocks)):
            if blocks[right] == "W":
                count += 1

            if blocks[right - k] == "W":
                count -= 1

            minimum = min(minimum, count)

        return minimum
