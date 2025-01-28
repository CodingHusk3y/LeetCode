class Solution:
    def findMaxFish(self, grid: List[List[int]]) -> int:
        maxFish = 0
        directions = [(0, 1), (1, 0), (-1, 0), (0, -1)]

        def dfs(graph, cell, visited):
            row, col = cell

            if cell in visited or graph[row][col] == 0:
                return 0

            curr = graph[row][col]
            visited.add(cell)

            for dr, dc in directions:
                nr, nc = row + dr, col + dc

                if nr in range(len(graph)) and nc in range(len(graph)):
                    curr += dfs(graph, (nr, nc), visited)

            return curr

        for row in range(len(grid)):
            for col  in range(len(grid[0])):
                if grid[col][row] > 0:
                    visited = set()
                    maxFish = max(maxFish, dfs(grid, (row, col), visited))

        return maxFish
            
