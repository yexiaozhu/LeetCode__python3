#！usr/bin/env python 3.6.5
# coding = utf-8
# author = yexiaozhu

import re
class Solution:
    def longestCommonPrefix(self, strs):
        """
        :param strs: List[str]
        :return: str
        """
        res = ""
        if len(strs) == 0:
            return ""
        print(zip(*strs))
        for each in zip(*strs):
            print(each)
            print(set(each))
            if len(set(each)) == 1:
                res += each[0]
            else:
                return res
        return res
        
    
if __name__ == '__main__':
    print(Solution().longestCommonPrefix(["flower","flow","flight"]))