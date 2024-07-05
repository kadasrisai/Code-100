# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def zigzagLevelOrder(self, root):
        result=[]
        if not root:
            return []
        queue = [root]
        level=0
        while queue:
            rev = []
            for i in range(len(queue)):
                curr = queue.pop(0)
                rev.append(curr.val)
                if curr.left:
                    queue.append(curr.left)
                if curr.right:
                    queue.append(curr.right)
            if level%2:
                result.append(rev[::-1])
            else: 
                result.append(rev)
            level += 1
        return result