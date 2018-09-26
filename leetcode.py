#！usr/bin/env python 3.6.5
# coding = utf-8
# author = yexiaozhu

import re
class Solution:
    def intToRoman(self, num):
        """
        :param num: int
        :return: str
        """
        if num > 3999 or num < 1:
            return 0
        num_tuple = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
        roman_tuple = ['M', 'CM', 'D', 'CD', 'C', 'XC', 'L', 'XL', 'X', 'IX', 'V', 'IV', 'I']
        result_str = ""
        for i in range(len(num_tuple)):
            while num >= num_tuple[i]:
                num -= num_tuple[i]
                # print(result_str)
                result_str += roman_tuple[i]
        return result_str
        
if __name__ == '__main__':
    print(Solution().intToRoman(58))