import math

def binarySearchHelper(a, t, q, r):
  if q > r:
    return False

  m = int(math.ceil((r - q)/2.0)) + q
  v = a[m]
  #print(" q: ",q, " r: ",r, " m: ",m, " v: ", v, " t: ", t)
  if v == t:
    return True
  elif v > t:
    return binarySearchHelper(a, t, q, m - 1)
  elif v < t:
    return binarySearchHelper(a, t, m + 1, r)
  

def binarySearch(a, t):
  return binarySearchHelper(a, t, 0, len(a) - 1)

# testing bin search
def testBinSearch(a, t, ans):
  actAns = binarySearch(a, t)
  if ans == actAns:
    return "Passed!"
  else:
    return "Did not pass: " + str(actAns) + " instead of " + str(ans) + " for " + str(t)

print(testBinSearch([], 2, False))
print(testBinSearch([0], 2, False))
print(testBinSearch([1,2,5,8,10], 1, True))
print(testBinSearch([1,2,5,8,10], 2, True))
print(testBinSearch([1,2,5,8,10], 3, False))

print(testBinSearch([1,2,5,8,10], 7, False))
print(testBinSearch([1,2,5,8,10], 8, True))
print(testBinSearch([1,2,5,8,10], 10, True))
print(testBinSearch([1,2,5,8,10], 100, False))

print(testBinSearch([1,2,5,8,10], 5, True))
print(testBinSearch([1,2,5,8,10], 2, True))
print(testBinSearch([1,2,5,8,10], -11, False))


