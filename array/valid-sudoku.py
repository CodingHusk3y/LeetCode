from typing import List

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        def isValid(xs):
            xs = list(filter(lambda x: x != '.', xs))  # Convert filter object to list
            return len(set(xs)) == len(xs)  # Check if all elements are unique

        # Validate rows and columns
        for i in range(9):
            # Validate rows
            if not isValid(board[i]):
                return False
            
            # Validate columns
            if not isValid([board[j][i] for j in range(9)]):
                return False
        
        # Validate 3x3 sub-grids
        for i in range(3):
            for j in range(3):
                subgrid = [board[m][n] for m in range(3*i, 3*i + 3) for n in range(3*j, 3*j + 3)]
                if not isValid(subgrid):
                    return False
        
        return True
