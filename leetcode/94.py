# type: Medium
# url: https://leetcode.com/problems/binary-tree-inorder-traversal/

from collections import deque
        
class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:  
        # Note: use popleft to treat a deque like a stack
        stack, arr, n = deque(), [], root
        
        while len(stack) > 0 or n != None:
            # traverse as far left as possible
            while n != None:
                stack.insert(0, n)
                n = n.left
            # get the most recent leftest most element
            n = stack.popleft()
            # add it to our answer
            arr.append(n.val)
            # move over the the leftmost elements right (to then traverse left again)
            n = n.right
            
        return arr
        
