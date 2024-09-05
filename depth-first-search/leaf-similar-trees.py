# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        def isLeaf(node):
            return not node.left and not node.right
        
        def bfs(root):         
            stk = [root]
            leave = []
            while stk:
                node = stk.pop()
                if isLeaf(node):
                    leave.append(node.val)
                if node.right:
                    stk.append(node.right)
                if node.left:
                    stk.append(node.left)

            return leave

        return bfs(root1) == bfs(root2)

