class neighborSum:

    def __init__(self, grid: List[List[int]]):
        self.grid = grid
        self.n = len(grid)
        # Create a dictionary to map value to its coordinates (i, j)
        self.value_to_coordinates = {}
        for i in range(self.n):
            for j in range(self.n):
                self.value_to_coordinates[grid[i][j]] = (i, j)


    def adjacentSum(self, value: int) -> int:
        if value not in self.value_to_coordinates:
            return 0
        x, y = self.value_to_coordinates[value]
        adjacent_sum = 0
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # Up, Down, Left, Right

        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < self.n and 0 <= ny < self.n:
                adjacent_sum += self.grid[nx][ny]
        
        return adjacent_sum

    def diagonalSum(self, value: int) -> int:
        if value not in self.value_to_coordinates:
            return 0
        x, y = self.value_to_coordinates[value]
        diagonal_sum = 0
        directions = [(-1, -1), (-1, 1), (1, -1), (1, 1)]  

        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < self.n and 0 <= ny < self.n:
                diagonal_sum += self.grid[nx][ny]
        
        return diagonal_sum


# Your neighborSum object will be instantiated and called as such:
# obj = neighborSum(grid)
# param_1 = obj.adjacentSum(value)
# param_2 = obj.diagonalSum(value)