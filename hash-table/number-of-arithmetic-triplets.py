class Solution:
    def arithmeticTriplets(self, nums: List[int], diff: int) -> int:
        count = 0
        seen = {}

        for i in range(len(nums)):
            seen[nums[i]] = 1

        for num in nums:
            if (num + diff) in seen and (num + diff + diff) in seen:
                count += 1
                
        return count