class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for row in range(len(board)):
            check = set()
            for i in range(len(board)):
                if board[row][i] == ".":
                    continue
                if board[row][i] in check:
                    return False
                else:
                    check.add(board[row][i])

        for col in range(len(board)):
            check = set()
            for j in range(len(board)):
                if board[j][col] == ".":
                    continue
                if board[j][col] in check:
                    return False
                else:
                    check.add(board[j][col])

        for square in range(9):
            check = set()
            for k in range(3):
                for f in range(3):
                    row = (square // 3) * 3 + k
                    col = (square % 3) * 3 + f

                    if board[row][col] == ".":
                        continue
                    if board[row][col] in check:
                        return False
                    else:
                        check.add(board[row][col])

        return True