class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans = []
        permu = []

        def backtrack(permu):
            if len(permu) == len(nums):
                ans.append(permu.copy())
                return

            for i in range(len(nums)):
                if nums[i] in permu:
                    continue
                permu.append(nums[i])
                backtrack(permu)
                permu.pop()

        backtrack(permu)
        return ans