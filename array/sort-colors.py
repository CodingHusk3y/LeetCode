class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        ptr1 = 0
        ptr2 = len(nums) - 1
        i = 0

        while i <= ptr2:
            if nums[i] == 0:
                nums[ptr1], nums[i] = nums[i], nums[ptr1]
                ptr1 += 1
                i += 1
            elif nums[i] == 2:
                nums[ptr2], nums[i] = nums[i], nums[ptr2]
                ptr2 -= 1
            else:
                i += 1

        