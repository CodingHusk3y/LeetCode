class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        letters = ('a', 'b', 'c')
        self.count = 0
        self.res = ""

        def backtrack(s):
            if len(s) == n:
                self.count += 1
                if self.count == k:
                    self.res = s
                return

            for letter in letters:
                if not s or s[-1] != letter:
                    backtrack(s + letter)
                    if self.res:
                        return 

        backtrack("")

        return self.res if self.res else ""