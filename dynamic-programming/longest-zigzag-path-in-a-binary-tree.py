# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestZigZag(self, root: Optional[TreeNode]) -> int:
        def helper(node, count, isLeft):
            if not node:
                return count

            left_count = helper(node.left, count + 1, True) if not isLeft else helper(node.left, 1, True)
            right_count = helper(node.right, count + 1, False) if isLeft else helper(node.right, 1, False)

            return max(left_count, right_count)

        if not root:
            return 0

        return max(helper(root.left, 1, True), helper(root.right, 1, False)) - 1