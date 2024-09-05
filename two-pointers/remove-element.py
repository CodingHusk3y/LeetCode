class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        ptr2 = len(nums) - 1 
        ptr1 = 0

        while ptr2 >= ptr1:
            if nums[ptr1] == val:
                nums[ptr1] = nums[ptr2]
                ptr2 -= 1
            else:
                ptr1 += 1

        return ptr1 