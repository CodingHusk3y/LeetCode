class Solution:
    def numOfSubarrays(self, arr: List[int]) -> int:
        mod = 10 ** 9 + 7
        curr_sum = 0
        odd = 0
        even = 0
        ans = 0

        for num in arr:
            curr_sum += num

            if curr_sum % 2 == 1:
                ans += 1 + even
                odd += 1
            else:
                ans += odd
                even += 1

        return ans % mod
            

                