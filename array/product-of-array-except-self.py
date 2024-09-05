class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        prefix = [1] * (n + 1)
        suffix = [1] * (n + 1)
        ans = []
        
        for i in range(1, n + 1):
            prefix[i] = prefix[i - 1] * nums[i - 1]
        for i in range(n - 1, -1, -1):
            suffix[i] = suffix[i + 1] * nums[i]

        for i in range(n):
            ans.append(prefix[i] * suffix[i + 1])

        return ans
