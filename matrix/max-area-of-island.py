class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0

        rows, cols = len(grid), len(grid[0])
        visited = set()
        max_area = 0

        def bfs(r, c):
            que = collections.deque()
            que.append((r, c))
            visited.add((r, c))
            directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
            area = 1

            while que:
                row, col = que.popleft()
                for dr, dc in directions:
                    r, c = row + dr, col + dc
                    if r in range(rows) and c in range(cols) and grid[r][c] == 1 and (r, c) not in visited:
                        area += 1
                        visited.add((r, c))
                        que.append((r, c))
            
            return area


        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1 and (r, c) not in visited:
                    curr_area = bfs(r, c)
                    max_area = max(max_area, curr_area)

        return max_area