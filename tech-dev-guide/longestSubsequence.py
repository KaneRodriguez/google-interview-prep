# TODO: read hints and solution given on page, implement

# https://techdevguide.withgoogle.com/paths/foundational/find-longest-word-in-dictionary-that-subsequence-of-given-string#!
def longestSub(S,D):
  longestWord = ""
  sLen = len(S)
  sIndex = 0
  for word in D:
    wLen = len(word)
    if wLen > sLen or wLen <= len(longestWord):
      continue
    
    sIndex = 0
    for i, wChar in enumerate(word):
      while(wChar != S[sIndex]):
        if sIndex == sLen - 1:
          break
        else:
          sIndex += 1

      if sIndex == sLen - 1 and wChar != S[sIndex]:
        break
      elif wLen - 1 == i:
        longestWord = word
      
  return longestWord
      
print(longestSub("abppple", ["able", "apple", "ale", "z"]))      
