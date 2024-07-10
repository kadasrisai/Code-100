# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isValidBST(self, root):
        def dfs(currentNode, minValue, maxValue):
            if not currentNode:
                return True
            
            if currentNode.val <= minValue or currentNode.val >= maxValue:
                 return False 

            return dfs(currentNode.left, minValue, currentNode.val) and dfs(currentNode.right, currentNode.val, maxValue)
        
        return dfs(root, float("-inf"), float("inf"))
        
        