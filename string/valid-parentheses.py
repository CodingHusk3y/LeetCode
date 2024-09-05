class Solution:
    def isValid(self, s: str) -> bool:
        def match(open, close):
            if (open == "(" and close == ")") or (open == "{" and close == "}") or (open == "[" and close == "]"):
                return True

        stk = []

        for char in s:
            if char in "({[":
                stk.append(char)
            else:
                if stk and match(stk[-1], char):
                    stk.pop()
                else:
                    return False
                
        return not stk


                
                
            
            


