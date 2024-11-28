class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        rows = len(image)
        cols = len(image[0])
        directions = [(0, 1), (1, 0), (-1, 0), (0, -1)]
        original = image[sr][sc]

        if image[sr][sc] == color:
            return image
        
        def dfs(r, c):
            if (r not in range(rows) or c not in range(cols) or image[r][c] != original):
                return
            image[r][c] = color
        
            for dr, dc in directions:
                dfs(r + dr, c + dc)

        dfs(sr, sc)
        return image
        

        