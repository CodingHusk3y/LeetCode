class Solution:
    def removeStars(self, s: str) -> str:
        stk = []
        for i in s:
            if i == "*":
                stk.pop()
            else:
                stk += [i]

        return "".join(stk)