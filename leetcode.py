#！usr/bin/env python 3.6.5
# coding = utf-8
# author = yexiaozhu

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
        
class Solution:
    def reverseKGroup(self, head, k):
        """
        :param head: ListNode
        :param k: int
        :return: ListNode
        """
        start = proNode = ListNode(0)
        start.next = l = r = head
        flag = True
        for i in range(k):
            if r:
                r = r.next
            else:
                return start.next
        while True:
            if not flag:
                return start.next
            cur, nextNode = l, r
            for i in range(k):
                if r:
                    r = r.next
                else:
                    flag = False
                cur.next, cur, nextNode = nextNode, cur.next, cur
            l, proNode.next, proNode = l.next, nextNode, l
        

