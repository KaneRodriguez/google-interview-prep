# type: easy
# url: https://leetcode.com/problems/find-all-numbers-disappeared-in-an-array/
# redo: True
# notes: Finding the solution that involved using no extra space proved difficult

import math

class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        final = []
        for index, num in enumerate(nums):
            i = abs(num) - 1
            nums[i] = -abs(nums[i])
        
        for index, num in enumerate(nums):
            if nums[index] > 0:
                final.append(index+1)
                
        return final
