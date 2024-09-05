class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        n = len(num)
        if n == k:
            return str(0)
        stk = []

        for digit in num:
            while k > 0 and stk and stk[-1] > digit:
                stk.pop()
                k -= 1

            stk.append(digit) 

        while k > 0:
            stk.pop()
            k-= 1

        result = ''.join(stk).lstrip('0')

        return result if result else '0'       
