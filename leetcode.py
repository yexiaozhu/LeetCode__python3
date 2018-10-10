#！usr/bin/env python 3.6.5
# coding = utf-8
# author = yexiaozhu

class Solution:
    def isValid(self, s):
        """
        :param s: str
        :return: bool
        """
        a = {')':'(', ']':'[', '}':'{'}
        l = [None]
        # print(len(l))
        for i in s:
            # print(i)
            if i in a and a[i] == l[-1]:
                # print(i, a[i], l, l[-1])
                l.pop()
            else:
                l.append(i)
        return len(l)==1
        

if __name__ == '__main__':
    print(Solution().isValid('()[]{}'))
    print(Solution().isValid(''))