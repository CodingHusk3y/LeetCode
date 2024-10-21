# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findFrequentTreeSum(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []

        freq = defaultdict(int)

        def post_order(node):
            if not node:
                return 0

            left_sum = post_order(node.left)
            right_sum = post_order(node.right)

            curr_sum = node.val + left_sum + right_sum

            freq[curr_sum] += 1
            
            return curr_sum

        post_order(root)
        max_freq = max(freq.values())

        return [sum_val for sum_val, count in freq.items() if count == max_freq]

        