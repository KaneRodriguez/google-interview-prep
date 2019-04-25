# Driver Code
m = [
  [1,2,3,4,5],
  [16,17,18,19,6],
  [15,24,25,20,7],
  [14,23,22,21,8],
  [13,12,11,10,9],
]

def rotMat(m):
  if m is None or len(m) == 0: return m
  N = len(m)

  # process each cycle
  for c in range(N//2):
    # process each position in each cycle 
    for s in range(c, N-c-1):
      tmp = m[c][c+s]
      m[c][c+s] = m[N-c-s-1][c]
      m[N-c-s-1][c] = m[N-c-1][N-c-s-1]
      m[N-c-1][N-c-s-1] = m[c+s][N-c-1]
      m[c+s][N-c-1] = m[c+s][N-c-1]
      m[c+s][N-c-1] = tmp 

def printMat(m):
  for row in m:
    print(row)

  print("\n")
  
printMat(m)
rotMat(m)
printMat(m)
