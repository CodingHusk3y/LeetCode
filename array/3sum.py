class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ans = []
        
        for i in range(len(nums) - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
                
            ptr1 = i + 1
            ptr2 = len(nums) - 1

            while ptr1 < ptr2:
                total = nums[i] + nums[ptr1] + nums[ptr2]
                
                if total < 0:
                    ptr1 += 1
                elif total > 0:
                    ptr2 -= 1
                else:
                    ans.append([nums[i], nums[ptr1], nums[ptr2]])

                    while ptr1 < ptr2 and nums[ptr1] == nums[ptr1 + 1]:
                        ptr1 += 1
                    while ptr1 < ptr2 and nums[ptr2] == nums[ptr2 - 1]:
                        ptr2 -= 1

                    ptr1 += 1
                    ptr2 -= 1

        return ans
                    
            
