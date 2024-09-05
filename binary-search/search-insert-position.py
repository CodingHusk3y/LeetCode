class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        ptr1, ptr2 = 0, len(nums) - 1
        while ptr1 <= ptr2:
            mid = ptr1 + (ptr2 - ptr1) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                ptr1 = mid + 1
            else:
                ptr2 = mid - 1
        return ptr1
            