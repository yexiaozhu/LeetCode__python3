#！usr/bin/env python 3.6.5
# coding = utf-8
# author = yexiaozhu

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
        
    def get_data(self):
        return self.data
        
class Solution:
    def removeNthFromEnd(self, head, n):
        """
        :param head: ListNode
        :param n: int
        :return: ListNode
        """
        list = []
        count = 0
        print(ListNode(0))
        while(head):
            list.append(head)
            head = head.next
            count += 1
        if count == 1:
            return None
        print(list)
        if list[-n].next == None:
            list[-n-1].next = None
            return list[0]
        else:
            list[-n].val = list[-n].next.val
            list[-n].next = list[-n].next.next
        return list[0]
        

if __name__ == '__main__':
    print(ListNode(1).val)
    # print(Solution().removeNthFromEnd([1,2,3,4,5], 2))