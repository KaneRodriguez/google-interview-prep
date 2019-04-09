# type: easy
# url: https://codingbat.com/prob/p119308
  
def has22(nums):
  last2 = False
  
  for n in nums:
    if n == 2:
      if last2:
        return True
      else:
        last2 = True
    else:
      last2 = False
  
  return False
