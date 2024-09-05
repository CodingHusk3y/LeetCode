from typing import List

class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        rows, cols = len(heights), len(heights[0])
        pac, atl = set(), set()

        def dfs(r, c, visit, prev_height):
            if (r, c) in visit or r < 0 or c < 0 or r >= rows or c >= cols or heights[r][c] < prev_height:
                return
            visit.add((r, c))
            for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                nr, nc = r + dr, c + dc
                dfs(nr, nc, visit, heights[r][c])

        # Start DFS from the Pacific Ocean (top and left borders)
        for c in range(cols):
            dfs(0, c, pac, heights[0][c])
        for r in range(rows):
            dfs(r, 0, pac, heights[r][0])
        
        # Start DFS from the Atlantic Ocean (bottom and right borders)
        for c in range(cols):
            dfs(rows - 1, c, atl, heights[rows - 1][c])
        for r in range(rows):
            dfs(r, cols - 1, atl, heights[r][cols - 1])
        
        # Collect the result
        result = []
        for r in range(rows):
            for c in range(cols):
                if (r, c) in pac and (r, c) in atl:
                    result.append([r, c])

        return result
