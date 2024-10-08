class Solution:
    def minDifference(self, nums: List[int]) -> int:
        nums.sort()
        change = nums[0]
        ans = 0

        if len(nums) <= 4:
            return 0

        ans = nums[-1] - nums[0]
        for i in range(4):
            ans = min(ans, nums[-(4 - i)] - nums[i])
        return ans