class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        empty = []
        for i in candies:
            if i + extraCandies >= max(candies):
                empty.append(True)
            else:
                empty.append(False)
        return empty
                