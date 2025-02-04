class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        ptr1 = 0
        longest = 1

        for ptr2 in range(1, len(nums)):
            if nums[ptr2] > nums[ptr2 - 1]:
                longest = max(longest, ptr2 - ptr1 + 1)
            else:
                ptr1 = ptr2

        ptr1 = 0  # Reset for decreasing sequence
        for ptr2 in range(1, len(nums)):
            if nums[ptr2] < nums[ptr2 - 1]:  # Decreasing sequence
                longest = max(longest, ptr2 - ptr1 + 1)
            else:
                ptr1 = ptr2  # Reset window when sequence breaks

        return longest
