"""
Remove Linked List Elements
  Go to Discuss
Remove all elements from a linked list of integers that have value val.

Example:

Input:  1->2->6->3->4->5->6, val = 6
Output: 1->2->3->4->5
"""
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """   
        # delete the first node if its value is val
        while head and head.val == val:
            head = head.next
            
        pre = None
        cur = head
        while cur:
            # delete cur node if found
            if cur.val == val:
                pre.next = cur.next
            else:
                pre = cur
            cur = cur.next
        return head