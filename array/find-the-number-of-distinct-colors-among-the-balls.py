class Solution:
    def queryResults(self, limit: int, queries: List[List[int]]) -> List[int]:
        ans = []
        color = {}  # Tracks position → color mapping
        color_count = defaultdict(int)  # Tracks how many times each color appears

        for pos, col in queries:
            if pos in color:
                old_col = color[pos]
                color_count[old_col] -= 1  # Decrease the old color count
                if color_count[old_col] == 0:
                    del color_count[old_col]  # Remove if it reaches zero

            color[pos] = col  # Update position's color
            color_count[col] += 1  # Increase new color count

            ans.append(len(color_count))  # Unique color count at this step

        return ans 
