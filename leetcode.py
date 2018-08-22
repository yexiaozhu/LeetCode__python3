#！usr/bin/env python 3.6.5
# coding = utf-8
# author = yexiaozhu

class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :param nums1: List[int]
        :param nums2: List[int]
        :return: float
        """
        nums1.extend(nums2)
        nums1.sort()
        k = len(nums1)
        if k % 2 == 1:
            q = k - 1
            p = nums1[int(q/2)]
        else:
            p = (nums1[int(k/2 -1)] + nums1[int(k/2)])/2
        print(p)
        return p
            
        
        
if __name__ == '__main__':
    # Solution().findMedianSortedArrays([1, 2], [3, 4])
    Solution().findMedianSortedArrays([1, 3], [2])