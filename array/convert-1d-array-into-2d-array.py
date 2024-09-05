class Solution:
    def construct2DArray(self, original: List[int], m: int, n: int) -> List[List[int]]:
        if len(original) != n * m:
            return []

        res = []

        for row in range(m):
            current_row = []
            start = row * n
            end = start + n
            for i in range(start, end):
                current_row.append(original[i])
            res.append(current_row)
            
        return res