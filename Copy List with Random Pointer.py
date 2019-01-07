'''
Copy List with Random Pointer
  Go to Discuss
A linked list is given such that each node contains an additional random pointer which could point to any node in the list or null.

Return a deep copy of the list.
'''
# Definition for singly-linked list with a random pointer.
class RandomListNode(object):
    def __init__(self, x):
        self.label = x
        self.next = None
        self.random = None

class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: RandomListNode
        :rtype: RandomListNode
        """
        if not head:
            return None
        
        l1 = []
        l2 = []
        
        # build copy to l2, just use next
        p1 = head
        prev = dummy = RandomListNode(-1)
        while p1:
            # create copy of p1, link to prev
            node = RandomListNode(p1.label)
            prev.next = node
            
            # add p1 to l1, add p2 to l2
            l1.append(p1)
            l2.append(node)
            
            # both move to next
            prev = prev.next
            p1 = p1.next
            
        # link random in l2
        p1 = head
        p2 = dummy.next
        while p1:
            if p1.random:
                index = l1.index(p1.random)
                p2.random = l2[index]
            p1 = p1.next
            p2 = p2.next
            
        return dummy.next