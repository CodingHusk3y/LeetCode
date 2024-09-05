class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        # have an ans
        # def func to take a multiple of a number until it is larger than targewe stop
        # while we adding the number itself into the combination, if we find another number 
            # that add up to target in the array, we can have the number itself multiple times and
                # the other number as a combination

        ans = []
        combination = []

        def backtrack(remain, start):
            if remain == 0:
                ans.append(combination.copy())
                return 

            if remain < 0:
                return

            for i in range(start, len(candidates)):
                combination.append(candidates[i])
                backtrack(remain - candidates[i], i)
                combination.pop()

        backtrack(target, 0)
        return ans
            

         