#！usr/bin/env python 3.6.5
# coding = utf-8
# author = yexiaozhu

import re
class Solution:
    def isMatch(self, s, p):
        """
        :param s: str
        :param p: str
        :return: bool
        """
        ans = (re.match(p, s))
        if (ans == None):
            return False
        if (ans.group(0) != s):
            return False
        return True
        
        
if __name__ == '__main__':
    print(Solution().isMatch("ab", ".*c"))