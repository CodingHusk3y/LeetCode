class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if target < matrix[0][0] or target > matrix[-1][-1]:
            return False

        Row = self.FindRow(matrix, target)
        left = 0
        right = len(matrix[Row]) - 1
        while left <= right:
            mid = (left + right) // 2
            if matrix[Row][mid] == target:
                return True
            elif matrix[Row][mid] < target:
                left = mid + 1
            else:
                right = mid - 1

        return False

    def FindRow(self, matrix, target):
        left = 0
        right = len(matrix) - 1
        while left <= right:
            row = (left + right) // 2
            if matrix[row][0] <= target <= matrix[row][-1]:
                return row
            if matrix[row][0] < target:
                left = row + 1
            elif matrix[row][-1] > target:
                right = row - 1

        return row

            