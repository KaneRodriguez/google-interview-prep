def magicIndex(A) -> bool:
  if not A: return False
  l, r = 0, len(A)-1

  while l <= r:
    m = (r-l)//2+l
    if m == A[m]:
      return True 
    elif A[m] > m:
      r = m - 1
    else:
      l = m + 1
  
  return False 

tests = [
  [[1,2,3,4,5,6,7],False],
  [[0,2,3,4,5,6,7],True],
  [[-3,0,1,6,7,10,15,16],False],
  [[-3,-1,0,2,3,4,6,16],True],
  ]

large_test = [i-1 for i in range(10000000)]
large_test[-1] = len(large_test)-1
tests.append([large_test, True])

for test_in, test_out in tests:
  if magicIndex(test_in) != test_out:
    print(f"Error! Expected {test_out}")
  else:
    print("Passed.")
