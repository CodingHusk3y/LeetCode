# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        def pathSumHelper(node, curr_sum, sum):
            if not node:
                return 0


            curr_sum += node.val

            # Check if the current path sum equals the target sum
            count = int(curr_sum == sum)

            # Recursively check the left and right subtrees
            count += pathSumHelper(node.left, curr_sum, sum)
            count += pathSumHelper(node.right, curr_sum, sum)

            return count

        if not root:
            return 0

        return pathSumHelper(root, 0, targetSum) + self.pathSum(root.left, targetSum) + self.pathSum(root.right, targetSum)
