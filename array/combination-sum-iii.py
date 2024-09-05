class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        if n < k:
            return []

        nums = [1,2,3,4,5,6,7,8,9]
        ans = []
        combi = []

        def backtrack(remain, k, start):
            if len(combi) == k and remain == 0:
                ans.append(combi.copy())
                return

                if remain < 0:
                    return 

            for i in range(start, len(nums)):
                if nums[i] in combi:
                    continue
                combi.append(nums[i])
                backtrack(remain - nums[i], k, i + 1)
                combi.pop()

        backtrack(n, k, 0)  
        return ans
