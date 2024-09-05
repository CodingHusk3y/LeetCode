class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        nums.sort()
        ans = []
        for i in range(len(nums)):
            ans.append(nums[i] + nums[-i-1])

        return max(ans)