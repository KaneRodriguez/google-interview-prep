# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# TODO: Do faster
# Medium
# https://leetcode.com/problems/insert-into-a-binary-search-tree/submissions/
class Solution:
    def insertIntoBST(self, root: TreeNode, val: int) -> TreeNode:
        newNode = TreeNode(val)
        if root is None:
            return newNode
        node = root

        while node is not None:
            if node.val < val:
                if node.right is None:
                    node.right = newNode
                    break
                else:
                    node = node.right
            else:
                if node.left is None:
                    node.left = newNode
                    break
                else:
                    node = node.left
                            
        return root
        
