from collections import deque

class TreeNode:
  def __init__(self, val):
    self.left = None
    self.right = None
    self.val = val
    self.level = None

class ListNode:
  def __init__(self, treeNode):
    self.val = treeNode.val
    self.next = None

def listOfDepths(root):
  if root is None:
    return []
  
  root.level = 0
  q = deque()
  depths = {}
  q.insert(0, root)

  while len(q) > 0:
    node = q.pop()
    listNode = ListNode(node)
    if not node.level in depths:
      depths[node.level] = [listNode, listNode]
    else:
      depths[node.level][1].next = listNode

      if depths[node.level][0].next == None:
        depths[node.level][0] = depths[node.level][1]

      depths[node.level][1] = depths[node.level][1].next
    
    if node.left != None:
      node.left.level = node.level + 1
      q.insert(0, node.left)
    if node.right != None:
      node.right.level = node.level + 1
      q.insert(0, node.right)

  return [se[0] for se in depths.values()]    

# testing

def testListOfDepths():
  # construct Tree
  root = TreeNode(5)
  root.left = TreeNode(2)
  root.right = TreeNode(8)
  root.left.left = TreeNode(7)
  root.left.right = TreeNode(6)
  root.left.right.right = TreeNode(4)
  root.right.left = TreeNode(3)
  
  res = listOfDepths(root)

  for r in res:
    while r is not None:
      print(r.val)
      r = r.next
    print("\n")

testListOfDepths()
