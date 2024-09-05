class Solution:
    def checkValidString(self, s: str) -> bool:
        open_b = []
        aster = []
        for i, ch in enumerate(s):
            # If current character is an open bracket, push its index onto the stack
            if ch == "(":
                open_b.append(i)
            # If current character is an asterisk, push its index onto the stack
            elif ch == "*":
                aster.append(i)
            # current character is a closing bracket ')'
            else:
                # If there are open brackets available, use them to balance the closing bracket
                if open_b:
                    open_b.pop()
                elif aster:
                    # If no open brackets are available, use an asterisk to balance the closing bracket
                    aster.pop()
                else:
                    # nnmatched ')' and no '*' to balance it.
                    return False

        while open_b and aster:
            # If an open bracket appears after an asterisk, it cannot be balanced, return false
            if open_b.pop() > aster.pop():
                return False  # '*' before '(' which cannot be balanced.

        # If all open brackets are matched and there are no unmatched open brackets left, return true
        return not open_b