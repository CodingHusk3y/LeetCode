class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operation = ['+', '-', '*', '/']
        stk = []
        for token in tokens:
            if token in operation:
                num2 = stk.pop()
                num1 = stk.pop()
                if token == '+':
                    stk.append(num1 + num2)
                elif token == '*':
                    stk.append(num1 * num2)
                elif token == '-':
                    stk.append(num1 - num2)
                else:
                    stk.append(int(num1 / num2))
            
            else:
                stk.append(int(token))

        return stk[0]