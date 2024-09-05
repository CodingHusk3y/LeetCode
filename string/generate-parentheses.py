class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        stk = []
        ans = []

        def backtrack(openN, closeN):
            if openN == closeN == n:
                ans.append(''.join(stk))
                return

            if openN < n:
                stk.append('(')
                backtrack(openN + 1, closeN)
                stk.pop()

            if openN > closeN:
                stk.append(')')
                backtrack(openN, closeN + 1)
                stk.pop()

        backtrack(0,0)

        return ans
