# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        def isLeaf(node):
            if not node.left and not node.right:
                return True
            
            return False 
        ans = []
        path = []

        def travel(node, path):
            if not node:
                return

            path.append(node.val)

            if isLeaf(node) and sum(path) == targetSum:
                ans.append(path[:])

            travel(node.left, path)
            travel(node.right, path)

            path.pop()

        travel(root, path)


        return ans     

