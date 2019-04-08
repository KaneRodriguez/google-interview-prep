# type: Easy
# url: https://leetcode.com/problems/to-lower-case/submissions/

# either use str.lower() method, use the below, or implement similar without the dict and just use the information about the offsets of the uppercase and lowercase letters
class Solution:
    def constructLowerMap(self):
        d = {}
        count = 0
        for i in range(ord('A'), ord('Z') + 1):
            d[chr(i)] = chr(ord('a') + count)
            count += 1
        return d
    
    def toLowerCase(self, str1: str) -> str:
        d = self.constructLowerMap()
        newStr = ""
        for i, c in enumerate(str1):
            if c in d:
                newStr += d[c]
            else:
                newStr += c
        return newStr
        
