# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root):
        if not root:
            return 0
        queue = [(root, 0)]
        max_width = 0
        while queue:
            level_size = len(queue)
            left_pos = queue[0][1]
            right_pos = queue[-1][1]
            max_width = max(max_width, right_pos - left_pos + 1)
            for i in range(level_size):
                node, pos = queue.pop(0)
                if node.left:
                    queue.append((node.left, pos*2))
                if node.right:
                    queue.append((node.right, pos*2 + 1))
            # Reset positions to avoid integer overflow
            for i in range(len(queue)):
                queue[i] = (queue[i][0], queue[i][1] - left_pos)
        return max_width
        