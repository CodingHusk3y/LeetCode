class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        if len(piles) == h:
            return max(piles)

        l, r = 1, max(piles)
        ans = r
        while l <= r:
            mid = (l + r) // 2
            hour = 0
            for pile in piles:
                hour += math.ceil(pile / mid)

            if hour <= h:
                ans = min(ans, mid)
                r = mid - 1
            else: 
                l = mid + 1

        return ans




        