class Solution:
    def numOfSubarrays(self, arr: List[int]) -> int:
        ans = 0
        mod = 10 ** 9 + 7
        for i in range(len(arr)):
            curr_sum = 0
            for j in range(i, len(arr)):
                curr_sum += arr[j]  
                if curr_sum % 2 == 1: 
                    ans += 1
                    
        return ans % mod
                