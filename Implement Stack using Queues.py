'''
Implement Stack using Queues
  Go to Discuss
Implement the following operations of a stack using queues.

push(x) -- Push element x onto stack.
pop() -- Removes the element on top of the stack.
top() -- Get the top element.
empty() -- Return whether the stack is empty.
Example:

MyStack stack = new MyStack();

stack.push(1);
stack.push(2);  
stack.top();   // returns 2
stack.pop();   // returns 2
stack.empty(); // returns false
Notes:

You must use only standard operations of a queue -- which means only push to back, peek/pop from front, size, and is empty operations are valid.
Depending on your language, queue may not be supported natively. You may simulate a queue by using a list or deque (double-ended queue), as long as you use only standard operations of a queue.
You may assume that all operations are valid (for example, no pop or top operations will be called on an empty stack).
'''
from collections import deque

class MyStack:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.queue = deque()

    def push(self, x):
        """
        Push element x onto stack.
        :type x: int
        :rtype: void
        """
        self.queue.append(x)
        self.rotate(self.size()-1)
        
    def pop(self):
        """
        Removes the element on top of the stack and returns that element.
        :rtype: int
        """
        if self.empty():
            return None 
        return self.queue.popleft()

    def top(self):
        """
        Get the top element.
        :rtype: int
        """
        if self.empty():
            return None
        return self.queue[0]

    def empty(self):
        """
        Returns whether the stack is empty.
        :rtype: bool
        """
        return self.size() == 0
    
    def size(self):
        return len(self.queue)

    def rotate(self, n):
        for _ in range(n):
            self.queue.append(self.queue.popleft())

class MyStack_1:
    import collections
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.queue = collections.deque()

    def push(self, x):
        """
        Push element x onto stack.
        :type x: int
        :rtype: void
        """
        self.queue.append(x)

    def pop(self):
        """
        Removes the element on top of the stack and returns that element.
        :rtype: int
        """
        if self.empty():
            return None 
        self.rotate(self.size()-1) # front to tail
        return self.queue.popleft()

    def top(self):
        """
        Get the top element.
        :rtype: int
        """
        if self.empty():
            return None
        self.rotate(self.size()-1) # rotate from front to tail
        result = self.queue[0]
        self.rotate(1)
        return result        

    def empty(self):
        """
        Returns whether the stack is empty.
        :rtype: bool
        """
        return self.size() == 0
    
    def size(self):
        return len(self.queue)

    def rotate(self, n):
        for _ in range(n):
            self.queue.append(self.queue.popleft())


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()