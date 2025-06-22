class Solution:
    def maxArea(self, height: List[int]) -> int:
        max_vol = 0
        ptr1 = 0
        ptr2 = len(height) - 1

        while ptr1 < ptr2:
            curr_vol = min(height[ptr1], height[ptr2]) * (ptr2 - ptr1)
            max_vol = max(curr_vol, max_vol)

            if height[ptr1] < height[ptr2]:
                ptr1 += 1
            else:
                ptr2 -= 1

        return max_vol

       
