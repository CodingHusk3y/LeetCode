class Solution:
    def maxWidthRamp(self, nums: List[int]) -> int:
        n = len(nums)
        stk = []

        for i in range(n):
            if not stk or nums[i] < nums[stk[-1]]:
                stk.append(i)

        max_ramp = 0
        for j in range(n - 1, -1, -1):
            while stk and nums[j] >= nums[stk[-1]]:
                i = stk.pop()
                max_ramp = max(max_ramp, j - i)

        return max_ramp