class Solution:
    def trap(self, height: List[int]) -> int:
        ptr1 = 0
        ptr2 = len(height) - 1
        left = height[ptr1]
        right = height[ptr2]
        count = 0

        while ptr1 <= ptr2:
            if left < right:
                count += left - height[ptr1]
                ptr1 += 1
                left = max(left, height[ptr1])

            else:
                count += right - height[ptr2]
                ptr2 -= 1
                right = max(right, height[ptr2])

        return count