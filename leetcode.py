#！usr/bin/env python 3.6.5
# coding = utf-8
# author = yexiaozhu

class Solution:
    def longestPalindrome(self, s):
        """
        :param s: str
        :return:  str
        """
        begin = end = 0
        table = []
        for i in range(len(s)):
            tem = []
            for j in range(len(s)):
                tem.append(0)
            table.append(tem)
        # print(table)
        for i in range(len(s)):
            table[i][i] = 1
        # print(table)
        for i in range(len(s) - 1):
            if s[i] == s[i+1]:
                table[i][i+1] = 1
                begin = i
                end = 1
                
        for tem in range(1, len(s)):
            for i in range(len(s) - tem):
                j = i+tem
                if (s[i]==s[j] and table[i+1][j-1]==1):
                    table[i][j] = 1
                    end = tem
                    begin = i
        # print(table)
        print(s[begin:begin+end+1])
        return s[begin:begin+end+1]
        
        
if __name__ == '__main__':
    Solution().longestPalindrome("babad")