#！usr/bin/env python 3.6.5
# coding = utf-8
# author = yexiaozhu

class Solution:
    def twoSum(self, nums, target):
        """
        :param nums: List[int]
        :param target: int
        :return: List[int]
        """
        d = {}
        for i, n in enumerate(nums):
            m = target - n
            # print(m)
            # print(d)
            if m in d:
                # print([d[m], i])
                return [d[m], i]
            else:
                d[n] = i
                
if __name__ == '__main__':
    Solution().twoSum([2, 7, 11, 15], 9)