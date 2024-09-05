# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        q = deque([root])
        store = {}
        level = 1

        while q:
            level_sum = 0
            curr_size = len(q) 

            for i in range(curr_size):
                node = q.popleft()
                level_sum += node.val

                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)

            store[level] = level_sum
            level += 1

        max_level = max(store, key=store.get)

        return max_level
                