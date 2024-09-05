class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        sorted_nums = sorted(nums)
        ptr1 = 0
        ptr2 = len(nums) - 1

        while ptr1 < ptr2:
            if sorted_nums[ptr1] + sorted_nums[ptr2] < target:
                ptr1 += 1
            elif sorted_nums[ptr1] + sorted_nums[ptr2] > target:
                ptr2 -= 1
            else:
                # Find the indices of the elements in the original nums list
                index1 = nums.index(sorted_nums[ptr1])
                index2 = nums.index(sorted_nums[ptr2])
                if index1 == index2:
                    index2 = nums.index(sorted_nums[ptr2], index1 + 1)
                return [index1, index2]