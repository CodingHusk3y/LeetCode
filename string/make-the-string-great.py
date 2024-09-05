class Solution:
    def makeGood(self, s: str) -> str:
        stk  = []
        for i in s:
        
            if stk and stk[-1] == i.swapcase():
                stk.pop()
            else:
                stk.append(i)

        return ''.join(stk)
