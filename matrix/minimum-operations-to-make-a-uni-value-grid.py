class Solution:
    def minOperations(self, grid: List[List[int]], x: int) -> int:
        nums = []
        ans = 0

        for row in grid:
            for num in row:
                nums.append(num)

        nums.sort()
        common_num = nums[len(nums) // 2]

        for num in nums:
            if common_num % x != num % x:
                return -1
            else:
                ans += abs(common_num - num) // x

        return ans
            