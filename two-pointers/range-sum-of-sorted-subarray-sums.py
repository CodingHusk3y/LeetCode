class Solution:
    def rangeSum(self, nums: List[int], n: int, left: int, right: int) -> int:
        mod = 10**9 + 7
        sub_total = []

        for start in range(len(nums)):
            curr = 0
            for end in range(start, len(nums)):
                curr += nums[end]
                sub_total.append(curr)

        sub_total.sort()
        return sum(sub_total[left - 1:right]) % mod

        