# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        s, b = sorted([p.val, q.val])
        while not s <= root.val <= b:
            # Keep searching since root is outside of [s, b].
            if s >= root.val:
                root = root.right  
            else:
                root = root.left
        # s <= root.val <= b.
        return root
