class Solution:
    def luckyNumbers (self, matrix: List[List[int]]) -> List[int]:
        ans = []
        for row in range(len(matrix)):
            row_min = min(matrix[row])
            min_index = matrix[row].index(row_min)
            lucky = True
            for same_row in range(len(matrix)):
                if matrix[same_row][min_index] > row_min:
                    lucky = False
                    break
                    
            if lucky:
                ans.append(row_min)
            
        return ans

                