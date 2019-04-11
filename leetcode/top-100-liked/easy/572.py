# type: easy
# url: https://leetcode.com/problems/subtree-of-another-tree/
# redo: True

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSubtree(self, s: TreeNode, t: TreeNode) -> bool:
        def equalNodes(n1: TreeNode, n2: TreeNode) -> bool:
            if n1 is None and n2 is None:
                return True
            elif n1 is None or n2 is None:
                return False
            return n1.val == n2.val and equalNodes(n1.left,n2.left) and equalNodes(n1.right,n2.right)
        
        def traverse(s1: TreeNode, t1: TreeNode) -> bool:
            return s1 != None and (equalNodes(s1,t1) or traverse(s1.left,t1) or traverse(s1.right, t1))
        
        return traverse(s,t)
