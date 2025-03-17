class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        count_set = Counter(nums)
        pair = 0

        for key in count_set:
            pair += count_set[key] // 2

        return pair == len(nums) // 2