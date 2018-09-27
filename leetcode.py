#！usr/bin/env python 3.6.5
# coding = utf-8
# author = yexiaozhu

import re
class Solution:
    def romanToInt(self, s):
        """
        :param s: str
        :return: int
        """
        num_tuple = [1000, 500, 100, 50, 10, 5, 1]
        roman_tuple = ['M', 'D','C', 'L', 'X', 'V', 'I']
        merge_dic = dict(zip(roman_tuple, num_tuple))
        print(merge_dic)
        num = 0
        for i in range(len(s) - 1):
            print(merge_dic[s[i]])
            if merge_dic[s[i]] < merge_dic[s[i+1]]:
                num -= merge_dic[s[i]]
            else:
                num += merge_dic[s[i]]
        num += merge_dic[s[-1]]
        return num
    
if __name__ == '__main__':
    print(Solution().romanToInt("IV"))