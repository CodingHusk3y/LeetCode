class Solution:
    def missingRolls(self, rolls: List[int], mean: int, n: int) -> List[int]:
        curr_total = sum(rolls)
        k = len(rolls) + n
        missing_total = mean * k - curr_total 

        if missing_total < 1 * n or missing_total > 6 * n:
            return []

        res = [1] * n
        missing_total -= n

        for i in range(n):
            adding = min(missing_total, 5)
            res[i] += adding
            missing_total -= adding
            if missing_total == 0:
                break

        return res
        
