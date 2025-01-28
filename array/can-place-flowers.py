class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        if n == 0:  # If no flowers need to be placed, return True immediately
            return True

        for i in range(len(flowerbed)):
            # Check if the current plot is empty and its neighbors are empty (or boundaries)
            if flowerbed[i] == 0 and (i == 0 or flowerbed[i - 1] == 0) and (i == len(flowerbed) - 1 or flowerbed[i + 1] == 0):
                flowerbed[i] = 1  # Place a flower
                n -= 1  # Decrease the remaining flowers to place
                if n == 0:  # Stop early if we've placed all flowers
                    return True

        return n == 0 