class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums) + 1
        sum_n = 0
        for i in range(n - 1):
            sum_n += i - nums[i]
        sum_n += n-1

        return sum_n