class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        ans = []
        max_candy = max(candies)

        for kid in candies:
            if kid + extraCandies >= max_candy:
                ans.append(True)
            else:
                ans.append(False)

        return ans
