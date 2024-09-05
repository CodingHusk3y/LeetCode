class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        ans = 0
        prefix = 0
        d = {0: 1}

        for num in nums:
            prefix += num

            if prefix - k in d:
                ans += d[prefix - k]

            if prefix in d:
                d[prefix] +=1
            else:
                d[prefix] = 1

        return ans