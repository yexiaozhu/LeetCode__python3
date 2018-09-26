#！usr/bin/env python 3.6.5
# coding = utf-8
# author = yexiaozhu

class Solution:
    def isPalindrome(self, x):
        """
        :param x:  int
        :return:  bool
        """
        if str(x) == str(x)[::-1]:
            return True
        else:
            return False
        
if __name__ == '__main__':
    print(Solution().isPalindrome("122"))