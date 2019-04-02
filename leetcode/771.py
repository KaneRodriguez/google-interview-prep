# https://leetcode.com/problems/jewels-and-stones/
class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:    
        # for every element in s, we check if it is in set(J) 
        # iterating through S is O(len(S))
        # lookup in set(J) is O(1) on average
        # Space complexity is O(len(J)) because of storing J in a set
        # technically, it is O(len(J) + len(S)) because we had to construct set J and iterate through S
        
        # the sum just adds up all of the True (found s values), this is our count
        return sum(s in set(J) for s in S)
