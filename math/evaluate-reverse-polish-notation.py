class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stk = []
        ops = "+-*/"

        for token in tokens:
            if token in ops and stk:
                num2 = stk.pop()
                num1 = stk.pop()
                res = 0

                if token == "+":
                    res = num1 + num2
                elif token == "-":
                    res = num1 - num2
                elif token == "*":
                    res = num1 * num2
                else:
                    res = int(num1 / num2)

                stk.append(res)

            else:
                stk.append(int(token))

        return stk[-1]