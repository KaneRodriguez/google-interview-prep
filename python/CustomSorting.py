# Playing with the sort function in python
data = ["tag 123", "tag2 cd def", "ohz bca", "older old gh", "newer 432", "new 123", "oha bca"]
# copy to new list
dataCopy = data.copy()

# print reverse
dataCopy.sort()
#print(dataCopy)

# copy to new list
dataCopy = data.copy()

def isNewer(a):
  # split element into its version and tag
  idNumber = a.split(" ")[0]
  version = a[len(idNumber)+1:]
  if not(ord('a') <= ord(version[0]) <= ord('z')):
    return True
  return False

def toVersionNumber(a):
  # split element into its version and tag
  idNumber = a.split(" ")[0]
  version = a[len(idNumber)+1:]
  return version + idNumber

dataCopy.sort(key=isNewer)

print("Sort by newer", dataCopy) 
olderVals = [val for val in dataCopy if not isNewer(val)]
newerVals = [val for val in dataCopy if isNewer(val)]
print("Split off newer", olderVals)
olderVals.sort(key=toVersionNumber)
print("Sort older", olderVals)
olderVals.extend(newerVals)
print("Result: ", olderVals)
