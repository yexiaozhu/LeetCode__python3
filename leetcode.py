#！usr/bin/env python 3.6.5
# coding = utf-8
# author = yexiaozhu

import re
class Solution:
    def threeSum(self, nums):
        """
        :param nums:  List[int]
        :return:  List[List[int]]
        """
        nums.sort()
        res = []
        lennums = len(nums)

        for i in range(lennums):
            left = i + 1
            right = lennums - 1
    
            if i > 0 and nums[i - 1] == nums[i]:
                left += 1
                continue
    
            while left < right:
                sumthree = nums[i] + nums[left] + nums[right]
                if sumthree == 0:
                    res_col = [nums[i], nums[left], nums[right]]
                    res.append(res_col)
                    left += 1
                    right -= 1
            
                    while nums[left] == nums[left - 1] and left < right:
                        left += 1
                    while nums[right] == nums[right + 1] and left < right:
                        right -= 1
        
                if sumthree < 0:
                    left += 1
                if sumthree > 0:
                    right -= 1
        return res
    
if __name__ == '__main__':
    print(Solution().threeSum([-1, 0, 1, 2, -1, -4]))
    print(Solution().threeSum([0,0,0,0]))
    print(Solution().threeSum([-2,0,1,1,2]))