class Solution:
    def minLength(self, s: str) -> int:
        stk = []

        for char in s:
            if stk and ((char == "B" and stk[-1] == "A") or (char == "D" and stk[-1] == "C")):
                stk.pop()
            else:
                stk.append(char)

        return len(stk)
            
