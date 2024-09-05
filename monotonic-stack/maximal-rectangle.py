class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        if not matrix:
            return 0

        rows, cols = len(matrix), len(matrix[0])
        height = [0] * (cols + 1)
        max_a = 0

        for row in matrix:
            for i in range(cols):
                height[i] = height[i] + 1 if row[i] == '1' else 0

            stk = []
            for i in range(len(height)):
                while stk and height[i] < height[stk[-1]]:
                    h = height[stk.pop()]
                    w = i if not stk else i - stk[-1] - 1
                    max_a = max(max_a, h * w)

                stk.append(i)

        return max_a

















