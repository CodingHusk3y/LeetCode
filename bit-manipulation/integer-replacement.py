class Solution:
    def __init__(self):
        self.memo = {}

    def recurse(self, n):
        if n == 1:
            return 0
        if n in self.memo:
            return self.memo[n]
        if n % 2 == 0:
            self.memo[n] = 1 + self.recurse(n // 2)
        else:
            self.memo[n] = 1 + min(self.recurse(n + 1), self.recurse(n - 1))
        return self.memo[n]

    def integerReplacement(self, n: int) -> int:
        return self.recurse(n)
