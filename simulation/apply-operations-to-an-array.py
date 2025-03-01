class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        for ptr1 in range(len(nums) - 1):
            ptr2 = ptr1 + 1
            
            if nums[ptr1] == nums[ptr2]:
                nums[ptr1] *= 2
                nums[ptr2] = 0

        ptr1 = 0
        for ptr2 in range(len(nums)):
            if nums[ptr2] != 0:
                nums[ptr1], nums[ptr2] = nums[ptr2], nums[ptr1]
                ptr1 += 1

        return nums