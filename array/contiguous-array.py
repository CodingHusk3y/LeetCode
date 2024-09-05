class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        ans = 0
        map_sum = {0: -1}
        max_length = 0
        for i in range(len(nums)):
            if nums[i] == 1:
                ans += 1
            else:
                ans -= 1
            
            if ans in map_sum:
                    max_length = max(max_length, i - map_sum[ans])
            else:
                map_sum[ans] = i

        return max_length 