'''
Implement Queue using Stacks
  Go to Discuss
Implement the following operations of a queue using stacks.

push(x) -- Push element x to the back of queue.
pop() -- Removes the element from in front of queue.
peek() -- Get the front element.
empty() -- Return whether the queue is empty.
Example:

MyQueue queue = new MyQueue();

queue.push(1);
queue.push(2);  
queue.peek();  // returns 1
queue.pop();   // returns 1
queue.empty(); // returns false
Notes:

You must use only standard operations of a stack -- which means only push to top, peek/pop from top, size, and is empty operations are valid.
Depending on your language, stack may not be supported natively. You may simulate a stack by using a list or deque (double-ended queue), as long as you use only standard operations of a stack.
You may assume that all operations are valid (for example, no pop or peek operations will be called on an empty queue).
'''
class MyQueue(object):
    import collections
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.stack_in = []
        self.stack_out = []

    def push(self, x):
        """
        Push element x to the back of queue.
        :type x: int
        :rtype: void
        """
        self.stack_in.append(x)

    # move elements from stack_in to stack_out
    def move(self):
        while self.stack_in:
            self.stack_out.append(self.stack_in.pop())
    
    def pop(self):
        """
        Removes the element from in front of queue and returns that element.
        :rtype: int
        """
        if self.empty():
            return None
        if not self.stack_out:
            self.move() # move elements from stack_in to stack_out
        return self.stack_out.pop()
        
    def peek(self):
        """
        Get the front element.
        :rtype: int
        """
        if self.empty():
            return None
        if not self.stack_out:
            self.move() # move elements from stack_in to stack_out
        return self.stack_out[-1]

    def empty(self):
        """
        Returns whether the queue is empty.
        :rtype: bool
        """
        # return not self.data and not self.help # not, if, while will do implicit bool conversion for self.data
        return len(self.stack_in)==0 and len(self.stack_out)== 0


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()