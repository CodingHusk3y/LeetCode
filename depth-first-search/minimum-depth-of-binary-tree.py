# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        def dfs(node):
            if not node:
                return float('inf')
            if not node.left and not node.right:
                return 1

            left_depth = dfs(node.left)
            right_depth = dfs(node.right)

            return 1 + min(left_depth, right_depth)

        if not root:
            return 0

        return dfs(root)