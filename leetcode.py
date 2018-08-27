#！usr/bin/env python 3.6.5
# coding = utf-8
# author = yexiaozhu

class Solution:
    def reverse(self, x):
        """
        :param x: int
        :return:  int
        """
        result = 0
        flag = 1
        if x < 0:
            x = -x
            flag = 0
        while(x):
            a = x%10
            result = result*10 + a
            # print(result)
            x = x//10
        if result>2**31-1 or result<-2**31:
            return 0
        else:
            if flag==0:
                return -result
            else:
                return result
        
if __name__ == '__main__':
    Solution().reverse(123)