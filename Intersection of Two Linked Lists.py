"""
 Intersection of Two Linked Lists
  Go to Discuss
Write a program to find the node at which the intersection of two singly linked lists begins.

For example, the following two linked lists:


begin to intersect at node c1.

 

Example 1:


Input: intersectVal = 8, listA = [4,1,8,4,5], listB = [5,0,1,8,4,5], skipA = 2, skipB = 3
Output: Reference of the node with value = 8
Input Explanation: The intersected node's value is 8 (note that this must not be 0 if the two lists intersect). From the head of A, it reads as [4,1,8,4,5]. From the head of B, it reads as [5,0,1,8,4,5]. There are 2 nodes before the intersected node in A; There are 3 nodes before the intersected node in B.
 

Example 2:


Input: intersectVal = 2, listA = [0,9,1,2,4], listB = [3,2,4], skipA = 3, skipB = 1
Output: Reference of the node with value = 2
Input Explanation: The intersected node's value is 2 (note that this must not be 0 if the two lists intersect). From the head of A, it reads as [0,9,1,2,4]. From the head of B, it reads as [3,2,4]. There are 3 nodes before the intersected node in A; There are 1 node before the intersected node in B.
 

Example 3:


Input: intersectVal = 0, listA = [2,6,4], listB = [1,5], skipA = 3, skipB = 2
Output: null
Input Explanation: From the head of A, it reads as [2,6,4]. From the head of B, it reads as [1,5]. Since the two lists do not intersect, intersectVal must be 0, while skipA and skipB can be arbitrary values.
Explanation: The two lists do not intersect, so return null.
 

Notes:

If the two linked lists have no intersection at all, return null.
The linked lists must retain their original structure after the function returns.
You may assume there are no cycles anywhere in the entire linked structure.
Your code should preferably run in O(n) time and use only O(1) memory.
"""
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        # find lenA of listA
        lenA, lenB = 0, 0
        curA, curB = headA, headB
        while curA is not None:
            lenA += 1
            curA = curA.next
            
        # find lenB of listB
        while curB is not None:
            lenB += 1
            curB = curB.next
        
        curA, curB = headA, headB
        # if lenA>lenB, curA moves forward (lenA-lenB)
        if lenA > lenB:
            for i in range(lenA-lenB):
                curA = curA.next
        # if lenB>lenA, curB moves forward (lenB-lenA)
        elif lenB > lenA:
            for i in range(lenB-lenA):
                curB = curB.next
        
        # curA, and curB moves foward, stop when meet, return curA
        while curA != curB:
            curA, curB = curA.next, curB.next
        return curA

class Solution2(object):
    def getIntersectionNode_0(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        if headA is None or headB is None:
            return None
        
        # 1.connect tail to headB, to form a cycle in linked list
        # 1.1 find tail
        tail = headB
        while tail.next is not None:
            tail = tail.next
            
        # 1.2 connect tail to headB, for a cycle
        tail.next = headB
        
        # 2.solve problem like "Linked List Cycle II"
        return self.detectCycle(headA, tail)
    
    def detectCycle(self, head, tail):
        # check whether there is cycle
        initNode = ListNode(None)
        initNode.next = head
        slow, fast = initNode, initNode
        while fast and fast.next:
            slow, fast = slow.next, fast.next.next
            if slow == fast:
                # if yes, find the position. H+D=nL
                while initNode != slow:
                    initNode, slow = initNode.next, slow.next
                tail.next = None
                return initNode
        
        tail.next = None
        return None