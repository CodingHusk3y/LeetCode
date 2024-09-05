from typing import List
import collections

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0

        rotten = collections.deque()
        rows, cols = len(grid), len(grid[0])
        fresh = 0
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

        # Collect initial rotten oranges and count fresh oranges
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    rotten.append((r, c))
                elif grid[r][c] == 1:
                    fresh += 1

        if fresh == 0:
            return 0  # No fresh oranges to rot

        minutes = 0

        while rotten and fresh > 0:
            minutes += 1
            for _ in range(len(rotten)):
                r, c = rotten.popleft()
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 1:
                        grid[nr][nc] = 2
                        fresh -= 1
                        rotten.append((nr, nc))

        return minutes if fresh == 0 else -1