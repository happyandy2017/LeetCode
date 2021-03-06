'''
Min Stack
  Go to Discuss
Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

push(x) -- Push element x onto stack.
pop() -- Removes the element on top of the stack.
top() -- Get the top element.
getMin() -- Retrieve the minimum element in the stack.
Example:
MinStack minStack = new MinStack();
minStack.push(-2);
minStack.push(0);
minStack.push(-3);
minStack.getMin();   --> Returns -3.
minStack.pop();
minStack.top();      --> Returns 0.
minStack.getMin();   --> Returns -2.
'''
class MinStack:
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = [] # store val
        self.min_stack = [] # store [minval, count]

    def push(self, x):
        """
        :type x: int
        :rtype: void
        """
        self.stack.append(x)
        if not self.min_stack or (x < self.min_stack[-1][0]):
            self.min_stack.append([x, 1])
        elif x == self.min_stack[-1][0]:
            self.min_stack[-1][1] += 1

    def pop(self):
        """
        :rtype: void
        """
        val = self.stack.pop()
        if val == self.min_stack[-1][0]:
            self.min_stack[-1][1] -= 1
            if self.min_stack[-1][1] == 0:
                self.min_stack.pop()

    def top(self):
        """
        :rtype: int
        """
        if len(self.stack) == 0:
            return -1
        return self.stack[-1]

    def getMin(self):
        """
        :rtype: int
        """
        if len(self.min_stack) == 0:
            return -1
        return self.min_stack[-1][0]

    
class MinStack1:
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []

    def push(self, x):
        """
        :type x: int
        :rtype: void
        """
        self.stack.append(x)

    def pop(self):
        """
        :rtype: void
        """
        if len(self.stack) == 0:
            return False
        self.stack.pop()
        return True

    def top(self):
        """
        :rtype: int
        """
        if len(self.stack) == 0:
            return -1
        return self.stack[-1]

    def getMin(self):
        """
        :rtype: int
        """
        if len(self.stack) == 0:
            return -1
        return min(self.stack)

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()