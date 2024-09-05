class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []
        combi = []
        candidates.sort()

        def bactrack(remain, start):
            if remain == 0:
                ans.append(combi.copy())
            if remain < 0:
                return 

            for i in range(start, len(candidates)):
                if i > start and candidates[i] == candidates[i - 1]:
                    continue
                combi.append(candidates[i])
                bactrack(remain - candidates[i], i + 1)
                combi.pop()

        bactrack(target, 0)
        return ans
                
                
        