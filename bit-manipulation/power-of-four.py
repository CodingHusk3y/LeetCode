class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        x = 0
        while 4**x <=n:
            if 4**x == n:
                return True
                break
            else:
                x += 1
                continue