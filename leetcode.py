#！usr/bin/env python 3.6.5
# coding = utf-8
# author = yexiaozhu

# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeTwoLists(self, l1, l2):
        """
        :param l1: ListNode
        :param l2: ListNode
        :return: ListNode
        """
        if l1 == None: return l2
        if l2 == None: return l1
        
        head = None
        if l1.val < l2.val:
            head = l1
            l1 = l1.next
        else:
            head = l2
            l2 = l2.next
        mylist = head
        while l1 != None and l2 != None:
            if l1.val < l2.val:
                mylist.next = l1
                l1 = l1.next
            else:
                mylist.next = l2
                l2 = l2.next
            mylist = mylist.next
        if l1 == None:
            mylist.next = l2
        else:
            mylist.next = l1
        return head
        
        

if __name__ == '__main__':
    print(Solution().isValid('()[]{}'))
    print(Solution().isValid(''))