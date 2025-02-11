class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        count = 0
        ptr1 = 0

        for ptr2 in range(len(nums)):
            if nums[ptr2] > nums[ptr1]:
                ptr1 = ptr2
                count += 1
            
        return count >= 2