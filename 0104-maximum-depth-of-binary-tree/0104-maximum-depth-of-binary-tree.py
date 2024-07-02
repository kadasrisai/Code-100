# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root is None:
            return 0
        
        # Find depth of left subtree
        left = self.maxDepth(root.left)
        
        # Find depth of right subtree
        right = self.maxDepth(root.right)
        
        # Return depth of current node
        return 1 + max(left, right)