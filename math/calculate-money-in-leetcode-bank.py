class Solution:
    def totalMoney(self, n: int) -> int:
        if n == 1:
            return 1
        a = 0
        sum = 0
        for i in range(n):
            if i%7 == 0:
                a = a + 1
            sum += a + (i%7) 
        return sum

