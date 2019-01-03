"""
Palindrome Linked List
  Go to Discuss
Given a singly linked list, determine if it is a palindrome.

Example 1:

Input: 1->2
Output: false
Example 2:

Input: 1->2->2->1
Output: true
Follow up:
Could you do it in O(n) time and O(1) space?
"""
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        # None or one node return True
        if not head or not head.next:
            return True
        
        # get length of linked list
        len = 0
        cur = head
        while cur:
            len += 1
            cur = cur.next
        
        # reverse the first half part
        pre = None
        cur = head
        for i in range(len//2):
            next = cur.next
            cur.next = pre
            pre, cur = cur, next
        
        # from the middle, left pointer->left, right pointer->right, check node one by one, if unequal, return False.
        # if all are equal, return True
        # if odd, cur move to next one step first
        if len % 2 == 1:
            cur = cur.next
        while cur:
            if pre.val != cur.val:
                return False
            pre, cur = pre.next, cur.next
        return True
    
    
head = ListNode(1)
head.next = ListNode(2)
Solution().isPalindrome(head)