# type: Medium
# url: https://leetcode.com/problems/range-sum-of-bst/
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def rangeSumBST(self, root: TreeNode, L: int, R: int) -> int:
        sum = 0
        if root is None:
            return 0
        if root.val >= L:
            sum += self.rangeSumBST(root.left, L, R)
        if root.val <= R:
            sum += self.rangeSumBST(root.right, L, R)
        if root.val >= L and root.val <= R:
            sum += root.val
        
        return sum
