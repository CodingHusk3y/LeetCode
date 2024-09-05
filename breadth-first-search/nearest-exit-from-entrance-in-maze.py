from collections import deque
from typing import List

class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        rows, cols = len(maze), len(maze[0])
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        
        # BFS initialization
        queue = deque([(entrance[0], entrance[1], 0)])  # (row, col, distance)
        maze[entrance[0]][entrance[1]] = '+'  # Mark the entrance as visited

        while queue:
            r, c, dist = queue.popleft()
            
            # Check if we've reached an exit
            if (r != entrance[0] or c != entrance[1]) and (r in [0, rows - 1] or c in [0, cols - 1]):
                return dist
            
            # Explore the neighbors
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if nr in range(rows) and nc in range(cols) and maze[nr][nc] == ".":
                    maze[nr][nc] = '+'  # Mark as visited
                    queue.append((nr, nc, dist + 1))

        return -1  # If no exit is found
