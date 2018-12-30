"""
Design Linked List
Design your implementation of the linked list. You can choose to use the singly linked list or the doubly linked list. A node in a singly linked list should have two attributes: val and next. val is the value of the current node, and next is a pointer/reference to the next node. If you want to use the doubly linked list, you will need one more attribute prev to indicate the previous node in the linked list. Assume all nodes in the linked list are 0-indexed.

Implement these functions in your linked list class:

get(index) : Get the value of the index-th node in the linked list. If the index is invalid, return -1.
addAtHead(val) : Add a node of value val before the first element of the linked list. After the insertion, the new node will be the first node of the linked list.
addAtTail(val) : Append a node of value val to the last element of the linked list.
addAtIndex(index, val) : Add a node of value val before the index-th node in the linked list. If index equals to the length of linked list, the node will be appended to the end of linked list. If index is greater than the length, the node will not be inserted.
deleteAtIndex(index) : Delete the index-th node in the linked list, if the index is valid.
Example:

MyLinkedList linkedList = new MyLinkedList();
linkedList.addAtHead(1);
linkedList.addAtTail(3);
linkedList.addAtIndex(1, 2);  // linked list becomes 1->2->3
linkedList.get(1);            // returns 2
linkedList.deleteAtIndex(1);  // now the linked list is 1->3
linkedList.get(1);            // returns 3
Note:

All values will be in the range of [1, 1000].
The number of operations will be in the range of [1, 1000].
Please do not use the built-in LinkedList library.
"""
# Definition for singly-linked list.
class Node(object):
    def __init__(self, val):
        self.val = val
        self.next = None

class MyLinkedList:            
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.head = None
        self.size = 0
        
    def get(self, index):
        """
        Get the value of the index-th node in the linked list. If the index is invalid, return -1.
        :type index: int
        :rtype: int
        """
        if index<0 or index>=self.size:
            return -1
        if not self.head:
            return -1
        
        cur = self.head
        for i in range(index):
            cur = cur.next

        return cur.val
    
    def addAtHead(self, val):
        """
        Add a node of value val before the first element of the linked list. After the insertion, the new node will be the first node of the linked list.
        :type val: int
        :rtype: void
        """
        cur = Node(val)
        cur.next = self.head
        self.head = cur
        
        self.size+=1

    def addAtTail(self, val):
        """
        Append a node of value val to the last element of the linked list.
        :type val: int
        :rtype: void
        """
        cur = Node(val)
        pre = self.head
        if not pre:
            self.head=cur
            self.size+=1
            return
        
        # find last node, as pre, none as next
        while pre.next:
            pre=pre.next
        # insert at last
        pre.next=cur
        
        self.size+=1


    def addAtIndex(self, index, val):
        """
        Add a node of value val before the index-th node in the linked list. If index equals to the length of linked list, the node will be appended to the end of linked list. If index is greater than the length, the node will not be inserted.
        :type index: int
        :type val: int
        :rtype: void
        """
        if index<0 or index>self.size:
            return
        
        if index == 0:
            self.addAtHead(val)
            return
            
        cur = Node(val)

        # find last node, as pre, none as next
        pre=self.head
        next=pre.next
        for i in range(index-1):           
            pre=next
            next=pre.next
            
        # insert at last
        cur.next=next
        pre.next=cur
        self.size+=1

    def deleteAtIndex(self, index):
        """
        Delete the index-th node in the linked list, if the index is valid.
        :type index: int
        :rtype: void
        """
        if index<0 or index>=self.size:
            return
        
        # Delete the First Node
        if index==0:
            self.head=self.head.next
            self.size-=1
            return
        
        pre=self.head
        next=pre.next
        for i in range(index-1):
            pre=next
            next=pre.next

        pre.next=next.next
        self.size-=1
# Your MyLinkedList object will be instantiated and called as such:
obj = MyLinkedList()
obj.addAtHead(1)
obj.addAtTail(3)
obj.addAtIndex(1,2)

param_1 = obj.get(1)
obj.deleteAtIndex(1)
param_1 = obj.get(1)

class MyLinkedList_Fastest:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.l=[]

    def get(self, index):
        """
        Get the value of the index-th node in the linked list. If the index is invalid, return -1.
        :type index: int
        :rtype: int
        """
        try: return self.l[index]
        except: return -1

    def addAtHead(self, val):
        """
        Add a node of value val before the first element of the linked list. After the insertion, the new node will be the first node of the linked list.
        :type val: int
        :rtype: void
        """
        self.l[:0]=[val]

    def addAtTail(self, val):
        """
        Append a node of value val to the last element of the linked list.
        :type val: int
        :rtype: void
        """
        self.l.append(val)

    def addAtIndex(self, index, val):
        """
        Add a node of value val before the index-th node in the linked list. If index equals to the length of linked list, the node will be appended to the end of linked list. If index is greater than the length, the node will not be inserted.
        :type index: int
        :type val: int
        :rtype: void
        """
        if index<=len(self.l): self.l[index:index]=[val]

    def deleteAtIndex(self, index):
        """
        Delete the index-th node in the linked list, if the index is valid.
        :type index: int
        :rtype: void
        """
        try: del(self.l[index])
        except: return
