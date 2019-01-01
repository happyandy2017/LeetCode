"""
Remove Nth Node From End of List
Given a linked list, remove the n-th node from the end of list and return its head.

Example:

Given linked list: 1->2->3->4->5, and n = 2.

After removing the second node from the end, the linked list becomes 1->2->3->5.
Note:

Given n will always be valid.

Follow up:

Could you do this in one pass?
"""
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        # init
        dummy = ListNode(-1)
        dummy.next = head
        slow, fast = dummy, dummy
        
        while n > 0 and fast.next:
            n -= 1
            fast = fast.next
            
        if n > 0:
            return dummy.next
        
        # slow, fast->end
        while fast and fast.next:
            slow, fast = slow.next, fast.next
            
        # delete node
        slow.next = slow.next.next
        
        return dummy.next