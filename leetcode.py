#！usr/bin/env python 3.6.5
# coding = utf-8
# author = yexiaozhu

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
        
class Solution:
    def mergeKLists(self, lists):
        """
        :param lists: List[ListNode]
        :return:  ListNode
        """
        res = []
        for i in lists:
            while i:
                res.append(i.val)
                i = i.next
        if res == []:
            return []
        res.sort()
        l = ListNode(0)
        first = l
        while res:
            l.next = ListNode(res.pop(0))
            l = l.next
        return first.next
        

