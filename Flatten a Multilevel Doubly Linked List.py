'''
Flatten a Multilevel Doubly Linked List
  Go to Discuss
You are given a doubly linked list which in addition to the next and previous pointers, it could have a child pointer, which may or may not point to a separate doubly linked list. These child lists may have one or more children of their own, and so on, to produce a multilevel data structure, as shown in the example below.

Flatten the list so that all the nodes appear in a single-level, doubly linked list. You are given the head of the first level of the list.

 

Example:

Input:
 1---2---3---4---5---6--NULL
         |
         7---8---9---10--NULL
             |
             11--12--NULL

Output:
1-2-3-7-8-11-12-9-10-4-5-6-NULL
 

Explanation for the above example:

Given the following multilevel doubly linked list:


 

We should return the following flattened doubly linked list:


'''
"""
# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""
class Solution:
    def flatten(self, head):
        """
        :type head: Node
        :rtype: Node
        """
        # important: need this one to guard
        if not head:
            return None
        
        pre = dummy = Node(-100, None, None, None)
        stack = [head]
        while stack:
            cur = stack.pop()
            # add cur to dummy (pre)
            pre.next = cur
            cur.prev = pre
            pre = cur
            
            if cur.next:
                stack.append(cur.next)
                cur.next = None
            if cur.child:
                # add cur.next to stack
                stack.append(cur.child)
                # important: set cur.child to None
                cur.child = None
                
        # important: cut relation with dummy node
        dummy.next.prev = None
        return dummy.next
'''
class Solution:
    def flatten(self, head):
        """
        :type head: Node
        :rtype: Node
        """
        # important: need this one to guard
        if not head:
            return None
        
        pre = dummy = Node(-100, None, None, None)
        stack = []
        cur = head
        while cur:
            # add cur to dummy (pre)
            pre.next = cur
            cur.prev = pre
            pre = cur
            if cur.child:
                # add cur.next to stack
                stack.append(cur.next)
                # important: set cur.child to None
                temp = cur
                cur = cur.child
                temp.child = None
            elif cur.next:
                cur = cur.next
            else:
                if len(stack) == 0:
                    break
                cur = stack.pop()
        # important: cut relation with dummy node
        dummy.next.prev = None
        return dummy.next
'''