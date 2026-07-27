"""
LeetCode 155. Min Stack

Problem:
Design a stack that supports push, pop, top, and retrieving
the minimum element in constant time.

Approach:
- Use two stacks:
    1. stack: Stores all values.
    2. minStack: Stores the minimum value at each level.
- Whenever a value is pushed:
    - Push it onto the main stack.
    - Push the smaller of the current value and the previous minimum
      onto the min stack.
- Whenever a value is popped:
    - Pop from both stacks.
- The top of minStack always contains the current minimum.

Time Complexity:
- push()   : O(1)
- pop()    : O(1)
- top()    : O(1)
- getMin() : O(1)

Space Complexity: O(n)
"""


class MinStack:

    def __init__(self):
        self.stack = []
        self.minStack = []

    def push(self, val: int) -> None:
        self.stack.append(val)

        if not self.minStack:
            self.minStack.append(val)
        else:
            self.minStack.append(min(val, self.minStack[-1]))

    def pop(self) -> None:
        self.stack.pop()
        self.minStack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minStack[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
