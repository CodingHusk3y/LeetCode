class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0

        visited = set()
        directions = [(0,1), (1,0), (-1,0), (0,-1)]
        island = 0
        rows, cols = len(grid), len(grid[0])

        def bfs(r, c):
            que = deque()
            visited.add((r, c))
            que.append((r, c))

            while que:
                (row, col) = que.popleft()
                
                for dr, dc in directions:
                    nr, nc = row + dr, col + dc
                    if nr in range(rows) and nc in range(cols) and grid[nr][nc] == "1" and (nr, nc) not in visited:
                        que.append((nr, nc))
                        visited.add((nr, nc))
        
        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == "1" and (row, col) not in visited:
                    bfs(row, col)
                    island += 1

        return island
        



