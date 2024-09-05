class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        row_dict = {}
        col_dict = defaultdict(list)
        ans = 0

        for row in range(len(grid)):
            row_dict[row] = grid[row]

        for col in range(len(grid)):
            for row in range(len(grid)):
                col_dict[col].append(grid[row][col])

        for row in row_dict.values():
            for col in col_dict.values():
                if row == col:
                    ans += 1

        return ans

        



