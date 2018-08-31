#！usr/bin/env python 3.6.5
# coding = utf-8
# author = yexiaozhu

class Solution:
    def myAtoi(self, str):
        """
        :param str: str
        :return: int
        """
        import re
        res = re.findall(r"^[\+\-]?\d+", str.strip())
        print(res)
        if res != []:
            if int(res[0]) > (2**31-1):
                return (2**31-1)
            if int(res[0]) < (-2**31):
                return (-2**31)
            return int(res[0])
        else:
            return 0
        
if __name__ == '__main__':
    print(Solution().myAtoi('-91283472332'))