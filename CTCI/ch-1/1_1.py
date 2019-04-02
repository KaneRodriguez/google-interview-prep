
def isUnique(str1):
  count = 0

  # check for valid string
  if type(str1) != str:
    return False
  # check for empty
  elif str1 is "":
    return True
  
  # loop through each lowercase letter, update count, return false if count raises above one for any given char
  for code in range(ord('a'), ord('z') + 1):
    for char in str1:
      if ord(char) == code:
        count += 1
      
      if count > 1:
        return False

    # reset count after each character is checked in str
    count = 0

  # all unique
  return True

# testing

for testVal in ["", None, [], "abc", "abbc", "xyz", "xyzz", "hell", "help"]:
  print(str(testVal) + ": " + str(isUnique(testVal)))
