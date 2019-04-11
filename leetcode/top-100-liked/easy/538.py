# type: easy
# url: https://leetcode.com/problems/convert-bst-to-greater-tree
# redo: True
# notes: redo with iterative solution
# timeToCode: 30 minutes

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def convertBST(self, root: TreeNode) -> TreeNode:
        def convertBSTHelper(node, gSum = 0):
            if node is None: return gSum
            
            node.val += convertBSTHelper(node.right, gSum)
            
            return convertBSTHelper(node.left, node.val)
        
        convertBSTHelper(root)
        
        return root
