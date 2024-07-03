# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self,root, p, q):
        if root is None: return None

        if root == p or root == q:
            left = self.lowestCommonAncestor(root.left, p, q)
            right = self.lowestCommonAncestor(root.right, p, q)
            return root
            
        left = self.lowestCommonAncestor(root.left, p,q)
        right = self.lowestCommonAncestor(root.right, p, q)
        if left is not None and right is not None: return root
        if left is not None and left == root.left: return left
        if right is not None and right == root.right : return right
        if left is not None: return left
        if right is not None: return right