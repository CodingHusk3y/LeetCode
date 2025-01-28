class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        if (flowerbed.count(0) - n) // n == 2: return True
        else: return False