# type: medium
# url: https://leetcode.com/problems/validate-binary-search-tree/
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isValidBST(self, root: TreeNode) -> bool:    
        def isBSTHelper(node: TreeNode, minV, maxV):
            if node is None:
                return True
            if minV != None and node.val <= minV:
                return False
            if maxV != None and node.val >= maxV:
                return False

            return isBSTHelper(node.left, minV, node.val) and isBSTHelper(node.right, node.val, maxV)
        
        return isBSTHelper(root, None, None)
