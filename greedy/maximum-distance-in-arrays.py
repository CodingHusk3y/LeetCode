class Solution:
    def maxDistance(self, arrays: List[List[int]]) -> int:
        curr_min, curr_max = arrays[0][0], arrays[0][-1]
        ans = 0

        for i in range(1, len(arrays)):
            array = arrays[i]
            ans = max(ans, max(array[-1] - curr_min, curr_max - array[0]))

            curr_min = min(curr_min, array[0])
            curr_max = max(curr_max, array[-1])

        return ans