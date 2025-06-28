class Solution:
    def isValid(self, s: str) -> bool:
        def match(open, close):
            return (open == "(" and close == ")") or (open == "{" and close == "}") or (open == "[" and close == "]")
        
        stk = []
        for string in s:
            if string in ["(", "{", "["]:
                stk.append(string)
            else:
                if not stk or not match(stk[-1], string):
                    return False
                stk.pop()

        return not stk



                
                
            
            


