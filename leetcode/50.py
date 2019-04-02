# Brute force solution, try again with fast power
# https://leetcode.com/problems/powx-n/solution/
# Also, this solution does not account for min max possible values of int/float
class Solution:
    def myPow(self, x: float, n: int) -> float:
        ans, flip = x, False
        if n == 0:
            return 1
        elif n < 0:
            flip = True
            n = abs(n)
        
        while n > 1:
            n -= 1
            ans *= x
        
        if flip:
            return 1 / ans
        else:
            return ans
