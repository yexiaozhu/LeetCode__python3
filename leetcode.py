#！usr/bin/env python 3.6.5
# coding = utf-8
# author = yexiaozhu

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
        
class Solution:
    def swapPairs(self, head):
        """
        :param head: ListNode
        :return: ListNode
        """
        if head == None:
            return head
        cur = ListNode(0)
        cur.next = head
        first = cur
        while cur.next and cur.next.next:
            n1 = cur.next
            n2 = n1.next
            nxt = n2.next
            n1.next = nxt
            n2.next = n1
            cur.next = n2
            cur = n1
        return first.next
        

