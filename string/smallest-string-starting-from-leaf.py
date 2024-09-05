# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def smallestFromLeaf(self, root: Optional[TreeNode]) -> str:
        def isLeaf(root):
            return not root.left and not root.right
        
        stk = []
        def dfs(root, lst):
            if not root:
                return []

            lst.append(chr(97+root.val))
            if isLeaf(root):
                stk.append("".join(lst[:]))
                return
                
            if root.left:
                dfs(root.left, lst)
                lst.pop()
            if root.right:
                dfs(root.right, lst)
                lst.pop()

        dfs(root, [])
        stk = sorted([i[::-1] for i in stk])
        return stk[0]