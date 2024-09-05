class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        counter = 0
        ans = 0
        for i in nums:
            if i == 1:
                counter += 1
            else:
                counter = 0
            ans = max(ans, counter)
            
            
        return ans