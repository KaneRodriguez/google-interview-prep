def hash(s, base):
  if not s: return 0
  return sum([ord(c)*base**(len(s)-1-i) for i,c in enumerate(s)])

def grep(haystack: str, needle: str):
  if not needle or not haystack: return []
  if len(needle) > len(haystack): return []

  hashBase, ans = 256, []
  hayHash, needleHash = 0, hash(needle, hashBase)

  for i in range(len(haystack)):
    print(i)
    if i < len(needle):
      hayHash = (hayHash*hashBase) + ord(haystack[i])
      # are we done constructing the first hash
      if i == len(needle) - 1 and needleHash == hayHash:
        if needle == haystack[:i+1]:
          # append 0 because this is the first index 
          ans.append(0)
    else:
      hayHash = (hayHash - ord(haystack[i-len(needle)])*hashBase**(len(needle)-1))*hashBase
      hayHash += ord(haystack[i])

      print(hayHash, needleHash)

      if needleHash == hayHash and needle == haystack[i-len(needle)+1:i+1]:
        ans.append(i-len(needle)+1)
  
  return ans

print(grep("bcbcbbccbbbcccb", "b"))
