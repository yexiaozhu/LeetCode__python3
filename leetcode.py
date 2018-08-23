#！usr/bin/env python 3.6.5
# coding = utf-8
# author = yexiaozhu

class Solution:
    def convert(self,s, numRows):
        """
        :param s:  str
        :param numRows: int
        :return:  str
        """
        if numRows == 1:
            return s
        zigzag = ['' for i in range(numRows)] # 初始化zigzag为['','','']
        row = 0
        step = 1
        for c in s:
            if row == 0:
                step = 1
            if row == numRows - 1:
                step = -1
            zigzag[row] += c
            # print(zigzag)
            row  +=  step
        return ''.join(zigzag)
        
if __name__ == '__main__':
    Solution().convert("PAYPALISHIRING", 3)