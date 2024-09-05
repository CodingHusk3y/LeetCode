class Solution:
    def maxArea(self, height: List[int]) -> int:
        ptr1 = 0
        ptr2 = len(height) - 1
        max_water = 0

        while ptr1 < ptr2:
            current = min(height[ptr1], height[ptr2]) * (ptr2 - ptr1)
            max_water = max(max_water, current)

            if height[ptr1] < height[ptr2]:
                ptr1 += 1
            else:
                ptr2 -= 1

        return max_water