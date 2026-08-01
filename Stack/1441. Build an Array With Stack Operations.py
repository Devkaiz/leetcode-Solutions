"""
LeetCode 1441. Build an Array With Stack Operations

Problem:
Given a target array and an integer n, return the sequence of
"Push" and "Pop" operations needed to build the target array
using numbers from 1 to n.

Approach:
- Iterate through the numbers from 1 to the maximum element
  in the target array.
- If the current number is in the target array,
  perform a "Push" operation.
- Otherwise, perform a "Push" followed by a "Pop" operation.
- Stop once the largest target element has been processed.

Time Complexity: O(max(target) × len(target))
Space Complexity: O(1) (excluding the output list)
"""

class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        out = []
        m = max(target)

        for i in range(1, m + 1):
            if i in target:
                out.append("Push")
            else:
                out.append("Push")
                out.append("Pop")

        return out
