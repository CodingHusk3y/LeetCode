class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        stk = []
        
        for char in s:
            if char == ")" and stk and stk[-1] == "(":
                stk.pop()
            else:
                stk.append(char)

        return len(stk)