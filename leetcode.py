#！usr/bin/env python 3.6.5
# coding = utf-8
# author = yexiaozhu

import re
class Solution:
    def maxArea(self, height):
        """
        :param height:  List[int]
        :return:  int
        """
        if height == []:
            return 0
        l = len(height)
        ans = 0
        
        p1 = 0
        p2 = l - 1
        while p1 < p2:
            ans = max(ans, min(height[p1], height[p2])*(p2-p1))
            if height[p1] < height[p2]:
                p1+=1
            else:
                p2-=1
        return ans
        
if __name__ == '__main__':
    print(Solution().maxArea([1,8,6,2,5,4,8,3,7]))