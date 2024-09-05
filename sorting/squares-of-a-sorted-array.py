class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        ans = []
        ptr1 = 0
        ptr2 = len(nums) - 1

        while ptr1 <= ptr2:
            left_square = nums[ptr1] ** 2
            right_square = nums[ptr2] ** 2
            if left_square > right_square:
                ans.append(left_square)
                ptr1 += 1
            else:
                ans.append(right_square)
                ptr2 -= 1

        return ans[::-1]

