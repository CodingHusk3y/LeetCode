class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        count = {0: 0, 1: 0}
        l = 0
        ans = 0

        for r in range(len(nums)):
            count[nums[r]] += 1

            while count[0] > k:
                count[nums[l]] -= 1
                l += 1

            ans = max(ans, r - l + 1)

        return ans
