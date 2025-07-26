class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m, n = len(matrix), len(matrix[0])
        ptr1, ptr2 = 0, m * n - 1

        while ptr1 <= ptr2:
            mid = (ptr1 + ptr2) // 2
            row = mid // n
            col = mid % n
            mid_value = matrix[row][col]

            if mid_value == target:
                return True
            elif mid_value < target:
                ptr1 = mid + 1
            else:
                ptr2 = mid - 1

        return False