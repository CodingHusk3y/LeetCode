class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        ptr1, ptr2 = 1, max(piles)
        ans = ptr2

        while ptr1 <= ptr2:
            mid = (ptr1 + ptr2) // 2
            finish = sum(math.ceil(pile / mid) for pile in piles)

            if finish <= h:
                ans = min(ans, mid)
                ptr2 = mid - 1
            else:
                ptr1 = mid + 1

        return ans