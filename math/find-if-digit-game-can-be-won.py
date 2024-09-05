class Solution:
    def canAliceWin(self, nums: List[int]) -> bool:
        total_sum = sum(nums)
        
        # Calculate sum of single-digit and double-digit numbers
        single_digit_sum = sum(x for x in nums if 1 <= x <= 9)
        double_digit_sum = sum(x for x in nums if 10 <= x <= 99)
        
        # Check if Alice can win by choosing all single-digit numbers
        return single_digit_sum > total_sum - single_digit_sum or double_digit_sum > total_sum - double_digit_sum

