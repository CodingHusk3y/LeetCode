class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        source_color = image[sr][sc]
        if source_color == color:
            return image

        directions = [[1, 0], [0, 1], [-1, 0], [0, -1]]

        def fill(x, y):
            if x < 0 or x >= len(image) or y < 0 or y >= len(image[0]) or image[x][y] != source_color:
                return

            image[x][y] = color

            for dx, dy in directions:
                fill(x + dx, y + dy)

        fill(sr, sc)
        return image
