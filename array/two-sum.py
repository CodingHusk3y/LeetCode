class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # 2 + 7 = 9
        # 7 = 9 - 2
        # 7: 0 -> 7 -> [1][0]
        # initial a hashmap
        # go through every number in array
        # at each number checking if there is already another number adding togother to make to the target
        # if not we logging the comliment and the position into the map

        tracking = {}

        for i in range(len(nums)):
            if nums[i] in tracking:
                return [i, tracking[nums[i]]]
            else:
                tracking[target - nums[i]] = i

            