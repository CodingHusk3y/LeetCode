class Solution:
    def partition(self, s: str) -> List[List[str]]:
        def checker(sub):
            return sub == sub[::-1]

        def backtrack(start, parti):
            if start == len(s):
                ans.append(parti.copy())
                return
            for end in range(start + 1, len(s) + 1):
                substring = s[start:end]
                if checker(substring):
                    parti.append(substring)
                    backtrack(end, parti)
                    parti.pop()

        ans = []
        parti = []
        backtrack(0, parti)
        return ans


