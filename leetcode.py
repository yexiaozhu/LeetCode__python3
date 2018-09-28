#！usr/bin/env python 3.6.5
# coding = utf-8
# author = yexiaozhu

import re
class Solution:
    def threeSumClosest(self, nums, target):
        """
        :param nums:  List[int]
        :param target: int
        :return: int
        """
        mindiff = 10000
        nums.sort()
        res = 0
        for i in range(len(nums)):
            left = i + 1
            right = len(nums) - 1
            while left < right:
                sum = nums[left] + nums[right] + nums[i]
                diff = abs(target - sum)
                if diff < mindiff:
                    mindiff = diff
                    res = sum
                if target == sum:
                    return sum
                elif sum < target:
                    left += 1
                else:
                    right -= 1
        return res


if __name__ == '__main__':
    print(Solution().threeSumClosest([-1, 2, 1, -4], 1))