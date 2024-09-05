import math

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l = 0
        max_price = 0

        for r in range(len(prices)):
            while prices[l] > prices[r]:
                l += 1

            max_price = max(max_price, prices[r] - prices[l])

        return max_price
