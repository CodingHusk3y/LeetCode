class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        nums.sort()
        longest = 0
        curr = 0
        for i in range(len(nums) - 1):
            if nums[i] + 1 == nums[i + 1]:
                curr += 1
                longest = max(longest, curr)
            else:
                curr = 0

        return longest + 1
                