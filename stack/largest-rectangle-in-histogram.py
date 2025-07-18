class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stk = []
        max_area = 0
        heights.append(0)

        for i, h in enumerate(heights):
            while stk and heights[stk[-1]] > h:
                height = heights[stk.pop()]
                width = i if not stk else i - stk[-1] - 1
                max_area = max(max_area, height * width)
            stk.append(i)

        return max_area