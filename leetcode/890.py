# Could improve. Instead of mapping  both the owrd and the pattern to a common format, could have made backwards mappings between them and checked for violations as running through the second map creation
# Also, there is a single map/set method which i didn't take the time to read
# https://leetcode.com/problems/find-and-replace-pattern/solution/
class Solution:
    def findAndReplacePattern(self, words: List[str], pattern: str) -> List[str]:
        pCode = self.getPCode(pattern)
        matches = []
        
        for word in words:
            wCode = self.getPCode(word)
            
            if wCode == pCode:
                matches.append(word)
        
        return matches
        
        
    def getPCode(self, word):
        pCode = ""
        count = 0
        codeMap = {}
        
        for char in word:
            if char in codeMap:
                pCode += codeMap[char]
            else:
                pCode += str(count)
                codeMap[char] = str(count)
                count += 1
        
        return pCode
