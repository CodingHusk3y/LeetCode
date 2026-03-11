class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_pos = [(num, pos) for pos, num in enumerate(nums)]

        num_pos.sort()

        ptr1 = 0
        ptr2 = len(nums) - 1

        while ptr1 < ptr2:
            if num_pos[ptr1][0] + num_pos[ptr2][0] < target:
                ptr1 += 1
            elif num_pos[ptr1][0] + num_pos[ptr2][0] > target:
                ptr2 -= 1
            else:
                return [num_pos[ptr1][1], num_pos[ptr2][1]]