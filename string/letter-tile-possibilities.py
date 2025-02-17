from collections import Counter

class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        def backtrack(counter):
            count = 0
            for tile in counter:
                if counter[tile] > 0:  # If we have any of this tile left
                    counter[tile] -= 1  # Choose this tile
                    count += 1 + backtrack(counter)  # Include it and explore further
                    counter[tile] += 1  # Undo choice (Backtrack)
            return count
        
        return backtrack(Counter(tiles))
           

            

