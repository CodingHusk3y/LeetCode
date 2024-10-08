class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        ans = []
        sub = []
        nums.sort()

        def backtrack(start):
            ans.append(sub.copy())

            for i in range(start, len(nums)):
                if i > start and nums[i] == nums[i - 1]:
                    continue
                sub.append(nums[i])
                backtrack(i + 1)
                sub.pop()

        backtrack(0)
        return ans