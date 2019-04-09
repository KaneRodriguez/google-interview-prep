# https://www.geeksforgeeks.org/set-bits-n-equals-m-given-range/

def b2D(n):
  return int(n, 2)

def d2B(n): 
    return bin(n).replace("0b","") 

def emplace(n, m, i, j):
    # number with all 1's 
    allOnes = not 0
   
    # Set all the bits in the left of j 
    left = allOnes << (j + 1) 
   
    # Set all the bits in the right of j 
    right = ((1 << i) - 1) 
   
    # Do Bitwsie OR to get all the bits  
    # set except in the range from i to j 
    mask = left | right 
   
    # clear bits j through i 
    masked_n = n & mask 
   
    # move m into the correct position 
    m_shifted = m << i 
   
    # return the Bitwise OR of masked_n  
    # and shifted_m 
    return (masked_n | m_shifted) 

print(emplace(b2D("10000000000"), b2D("10011"), 2, 6))
print(b2D("10001001100"))

# Drivers program 
n, m = 2, 4
i, j = 2, 4
print(emplace(n, m, i, j))
