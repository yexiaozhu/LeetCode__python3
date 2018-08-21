#！usr/bin/env python 3.6.5
# coding = utf-8
# author = yexiaozhu

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def addTwoNumbers(self, l1, l2):
        """
        :param l1:  ListNode
        :param l2:  ListNode
        :return:  ListNode
        """
        if l1 == None: return l2
        if l2 == None: return l1
        dummy_head = ListNode(0)
        pt = dummy_head  # 指针
        carry = 0  # 进位
        while l1 or l2 or carry:
            sum, carry = carry, 0
            print("sum:", sum)
            if l1:
                sum += l1.val
                l1 = l1.next
                # print(l1)
                print("suml1:", sum)
            if l2:
                sum += l2.val
                l2 = l2.next
                # print(l2)
                print("suml2:", sum)
            if sum > 9:
                carry = 1
                sum -= 10
            pt.next = ListNode(sum)
            pt = pt.next
            # print("pt:",pt)
            # print("listNodeToString(pt):",listNodeToString(pt))
        return dummy_head.next