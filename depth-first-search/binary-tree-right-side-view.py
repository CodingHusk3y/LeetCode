# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return []

        ans = []
        q = deque([root])

        while q:
            size = len(q)
            right = None  # To store the rightmost node at each level

            for i in range(size):
                node = q.popleft()
                if node:
                    right = node  # Update rightmost node value

                    # Enqueue right child first, then left child
                    if node.left:
                        q.append(node.left)
                    if node.right:
                        q.append(node.right)

            if right is not None:
                ans.append(right.val)

        return ans

       
                    


            