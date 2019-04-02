# distinct index mapping solution (can do faster if not having to worry about each element in B . being mapped to by an element in A)
# https://leetcode.com/problems/find-anagram-mappings/solution/
class Solution:
    def anagramMappings(self, A: List[int], B: List[int]) -> List[int]:
        T, P = dict(), [None]*len(A)
        for i, a in enumerate(A):
            if a in T:
                T[a].append(i)
            else:
                T[a] = list([i])
        for i, b in enumerate(B):
            P[T[b][0]] = i
            T[b].pop(0)
        return P
