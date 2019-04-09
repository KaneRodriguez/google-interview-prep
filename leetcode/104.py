# type: easy
# url: https://leetcode.com/problems/maximum-depth-of-binary-tree/submissions/
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        return self.maxDepthHelper(root, 1)
    
    def maxDepthHelper(self, node: TreeNode, cur: int) -> int:
        if node is None:
            return cur - 1
        cur += 1
        return max(self.maxDepthHelper(node.left, cur), self.maxDepthHelper(node.right, cur))
