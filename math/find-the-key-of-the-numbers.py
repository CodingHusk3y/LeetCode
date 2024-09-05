class Solution:
    def generateKey(self, num1: int, num2: int, num3: int) -> int:
        def padding(num):
            num = str(num)
            while len(num) < 4:
                num = '0' + num

            return num

        num1 = padding(num1)
        num2 = padding(num2)
        num3 = padding(num3)

        key = ""

        for i in range(0, 4):
            key += min(num1[i], num2[i], num3[i])

        return int(key)


