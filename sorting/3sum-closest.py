class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        if len(nums) == 3:
            return sum(nums)

        closest = float(inf)
        nums.sort()

        for i in range(len(nums) - 2):
            j = i + 1
            k = len(nums) - 1

            while j < k:
                total = nums[i] + nums[j] + nums[k]

                if abs(total - target) < abs(closest - target):
                    closest = total

                if total > target:
                    k -= 1
                elif total < target:
                    j += 1
                else: 
                    return total

        return closest

                

