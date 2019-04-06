class TreeNode:
  def __init__(self, val):
    self.val = val
    self.right = None
    self.left = None

# Note: this solution requires O(n) time AND O(n) stack space. TODO: make iterative
def createMinBST(array):
  return _createMinBST(array, 0, len(array) - 1)

def _createMinBST(array, start, end):
  # iterate through left and right, creating subtrees 
  # in O(n) time, making the mid the middle of this section

  mid = (start + end) // 2
  node = TreeNode(array[mid])

  # recurse through the subtrees
  if end < start:
    return None

  # print("Start Mid End: " + str(start) + " " + str(mid) + " " + str(end))
  node.left = _createMinBST(array, start, mid - 1)
  node.right = _createMinBST(array, mid + 1, end)

  return node

def inOrderTraversal(root):
  if root is not None:
    inOrderTraversal(root.left)
    print(root.val)
    inOrderTraversal(root.right)

# testing
def testCreateMinBST():
  # should print out: 1, 2, 3, 4, 5, 6, 7, 8
  inOrderTraversal(createMinBST([1, 2, 3, 4, 5, 6, 7, 8]))

testCreateMinBST()
