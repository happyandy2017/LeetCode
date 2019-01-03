"""
Odd Even Linked List
  Go to Discuss
Given a singly linked list, group all odd nodes together followed by the even nodes. Please note here we are talking about the node number and not the value in the nodes.

You should try to do it in place. The program should run in O(1) space complexity and O(nodes) time complexity.

Example 1:

Input: 1->2->3->4->5->NULL
Output: 1->3->5->2->4->NULL
Example 2:

Input: 2->1->3->5->6->4->7->NULL
Output: 2->3->6->7->1->5->4->NULL
Note:

The relative order inside both the even and odd groups should remain as it was in the input.
The first node is considered odd, the second node even and so on ...
"""
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def oddEvenList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return None
        
        cur1, cur2, head2 = head, head.next, head.next
        while cur1 and cur1.next and cur2 and cur2.next:
            cur1.next = cur1.next.next
            cur2.next = cur2.next.next
            
            cur1 = cur1.next
            cur2 = cur2.next
        cur1.next = head2
        return head
            
class Solution_Fast:
    def oddEvenList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        dummy1 = ListNode(0)
        dummy2 = ListNode(0)
        dummy1.next = dummy2
        dummy2.next = head
        
        p1 = dummy1
        p2 = dummy2
        
        move1 = True
        while p1.next and p2.next:
            if move1:
                p1.next = p2.next
                p1 = p1.next
            else:
                p2.next = p1.next
                p2 = p2.next
            move1 = not move1
            
        p2.next = None
        p1.next = dummy2.next
        return dummy1.next