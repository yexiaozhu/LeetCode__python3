#！usr/bin/env python 3.6.5
# coding = utf-8
# author = yexiaozhu

class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        :param s: str
        :return:  int
        """
        start = 0
        max_length = 0
        substring = {}
        for i, c in enumerate(s):
            if c in substring and start <= substring[c]:#只有当重复值是在start后面出现时才移动start
                start = substring[c] + 1
                print(substring)
            else:
                max_length = max(max_length, i - start + 1)
            substring[c] = i
            
        return max_length
    
if __name__ == '__main__':
    Solution().lengthOfLongestSubstring("abcabcbb")