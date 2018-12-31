"""
Linked List Cycle II
  Go to Discuss
Given a linked list, return the node where the cycle begins. If there is no cycle, return null.

To represent a cycle in the given linked list, we use an integer pos which represents the position (0-indexed) in the linked list where tail connects to. If pos is -1, then there is no cycle in the linked list.

Note: Do not modify the linked list.

 

Example 1:

Input: head = [3,2,0,-4], pos = 1
Output: tail connects to node index 1
Explanation: There is a cycle in the linked list, where tail connects to the second node.


Example 2:

Input: head = [1,2], pos = 0
Output: tail connects to node index 0
Explanation: There is a cycle in the linked list, where tail connects to the first node.


Example 3:

Input: head = [1], pos = -1
Output: no cycle
Explanation: There is no cycle in the linked list.


 

Follow up:
Can you solve it without using extra space?
"""

"""
Consider the following linked list, where E is the cylce entry and X, the crossing point of fast and slow.
        H: distance from head to cycle entry E
        D: distance from E to X
        L: cycle length
                          _____
                         /     \
        head_____H______E       \
                        \       /
                         X_____/   
        
    
        If fast and slow both start at head, when fast catches slow, slow has traveled H+D and fast 2(H+D). 
        Assume fast has traveled n loops in the cycle, we have:
        2H + 2D = H + D + nL  -->  H + D = nL  --> H = nL - D
        Thus if two pointers start from head and X, respectively, one first reaches E, the other also reaches E. 
        In my solution, since fast starts at head.next, we need to move slow one step forward in the beginning of part 2
"""
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):   
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        initNode = ListNode(None)
        initNode.next = head
        slow, fast = initNode, initNode
        while fast and fast.next:
            slow, fast = slow.next, fast.next.next
            if slow == fast:
                while initNode != slow:
                    initNode, slow = initNode.next, slow.next
                return(slow)
            
        return(None)
    
    def detectCycle_2(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        # check whether there is cycle
        try:
            slow = head
            fast = head.next
            while slow is not fast:
                slow = slow.next
                fast = fast.next.next    
        # if there is an exception, we reach the end and there is no cycle
        except:
            return None
        
        # find the starting node
        # since fast starts at head.next, we need to move slow one step forward
        slow = slow.next
        while slow is not head:
            slow = slow.next
            head = head.next
        return slow