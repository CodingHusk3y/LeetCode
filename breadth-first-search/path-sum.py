# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        def isLeaf(node):
            if node.left is None and node.right is None:
                return True
            return False

        def travel(node, total):
            if node is None:
                return False

            total += node.val

            if isLeaf(node) and total == targetSum:
                return True

            return travel(node.left, total) or travel(node.right, total)

        return travel(root, 0)
            
        
            
            