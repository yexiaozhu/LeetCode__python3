#！usr/bin/env python 3.6.5
# coding = utf-8
# author = yexiaozhu

class Solution:
    def generateParentheses(self, n):
        """
        :param n: int
        :return: List[str]
        """
        res = []
        self.generate(n, n, "", res)
        return res
    
    def generate(self, left, right, str, res):
        if left == 0 and right == 0:
            res.append(str)
            print(res)
            return
        if left > 0:
            print('left:', left, str)
            self.generate(left-1, right, str+'(', res)
        if right > left:
            print('right', right, str)
            self.generate(left, right-1, str+')', res)
            
if __name__ == '__main__':
    print(Solution().generateParentheses(3))

        

