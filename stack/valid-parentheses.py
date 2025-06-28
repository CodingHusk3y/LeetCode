class Solution:
    def isValid(self, s: str) -> bool:
        def match(open, close):
            return (open == "(" and close == ")") or (open == "{" and close == "}") or (open == "[" and close == "]")
        
        stk = []
        for string in s:
            if string in ["(", "{", "["]:
                stk.append(string)
            else:
                if not match(stk[-1], string) or not stk:
                    return False
                stk.pop()

        return not stk



                
                
            
            


