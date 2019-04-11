# type: Easy
# url: https://leetcode.com/problems/shortest-unsorted-continuous-subarray
# redo: True

class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        l, r, maxV, minV = 0, 0, None, None
        # 1. find where the array first messes up: left to right
        #       * take the min value of the range between first mess up and end of the array
        for i in range(1, len(nums)):
            if nums[i] < nums[i-1]:
                minV = min(nums[i:])
                break
        
        # there was not a messup! return 0
        if minV is None:
            return 0
        
        # 2. find where the array first messes up: right to left
        #       * take the max value of the range between first messup and beginning of array
        for i in range(len(nums)-2,-1,-1):
            if nums[i] > nums[i+1]:
                maxV = max(nums[0:i+1])
                break
                
        if maxV is None:
            return 0
        
        # 3. find the position for the min element in the array
        for i in range(len(nums)):
            if minV < nums[i]:
                l = i
                break
        # 4. find the position for the max element in the array
        for i in range(len(nums)-1,-1,-1):
            if maxV > nums[i]:
                r = i
                break
                
        # return 0 if the right index crossed over the left
        if r - l < 0:
            return 0
        # the inclusive difference between the indices is the result
        else:
            return r - l + 1
