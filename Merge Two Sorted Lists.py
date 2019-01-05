'''
Merge Two Sorted Lists
  Go to Discuss
Merge two sorted linked lists and return it as a new list. The new list should be made by splicing together the nodes of the first two lists.

Example:

Input: 1->2->4, 1->3->4
Output: 1->1->2->3->4->4
'''
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        p1, p2 = l1, l2
        dummy = ListNode(-1)
        p3 = dummy
        # find one node
        while p1 and p2:
            if p1.val <= p2.val:
                # add p1 to l3
                p3.next = p1
                p3 = p1
                p1 = p1.next
            else:
                # add p2 to l3
                p3.next = p2
                p3 = p2
                p2 = p2.next
        if p1:
            # link p1 and next nodes to l3
            p3.next = p1
        
        if p2:
            # add p2 to l3
            p3.next = p2
        
        return dummy.next