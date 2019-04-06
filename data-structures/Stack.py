# implementing a stack with: pop, insert, peek, isEmpty
class StackNode:
  def __init__(self, value):
    self._value = value
    self._next = None

class Stack:
  def __init__(self, elements = []):
    self.top = None
    for el in elements:
      self.insert(el)
    
  def insert(self, value):
    node = StackNode(value)
    node._next = self.top
    self.top = node

  def peek(self):
    if self.isEmpty():
      # raise error?
      return None
    else:
      return self.top._value


  def pop(self):
    if self.isEmpty():
      #raise error?
      return None
    else:
      val = self.top._value
      self.top = self.top._next
      return val
  
  def isEmpty(self):
    return True if self.top is None else False
  
def testStack():
  testList = [1, 2, 3, 9, 3, 1, 7, 4, 5]
  stack = Stack(testList)

  top = stack.pop()
  i = 0
  testList = testList[::-1]

  while top != None:
    print("Stack: " + str(top) + " Expected: " + str(testList[i]))
    i += 1
    top = stack.pop()

testStack()
