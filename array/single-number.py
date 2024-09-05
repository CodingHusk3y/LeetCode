class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        c = {}
        for i in nums:
            if i not in c:
                c[i] = 1
            else:
                c[i] += 1
        return min(c, key = c.get)