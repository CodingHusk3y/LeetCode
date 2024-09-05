class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = {}

        for i in nums:
            count[i] = 1 + count.get(i, 0)
        
        major = len(nums) // 2

        for num in count:
            if count[num] > major:
                return num 
            