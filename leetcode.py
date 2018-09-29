#！usr/bin/env python 3.6.5
# coding = utf-8
# author = yexiaozhu

import re
class Solution:
    def letterCombination(self, digits):
        """
        :param digits:  str
        :return:  List[str]
        """
        if not digits:
            return []
        digit2chars = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz'
        }
        res = [i for i in digit2chars[digits[0]]]
        print(res)
        for i in digits[1:]:
            print(i)
            print(digit2chars[i])
            res = [m+n for m in res for n in digit2chars[i]]
            print(res)
        return res
    
if __name__ == '__main__':
    print(Solution().letterCombination("2342"))