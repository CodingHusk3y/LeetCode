# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def distributeCoins(self, root: Optional[TreeNode]) -> int:
        self.moves = 0

        def dfs(current):
            if current == None:
                return 0

            left = dfs(current.left)
            right = dfs(current.right)

            self.moves += abs(left) + abs(right)

            return (current.val - 1) + left + right

        dfs(root)

        return self.moves