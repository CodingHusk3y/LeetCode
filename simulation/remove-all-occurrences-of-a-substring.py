class Solution:
    def removeOccurrences(self, s: str, part: str) -> str:
        stk = []
        part_length = len(part)

        for char in s:
            stk.append(char)

            if len(stk) >= part_length and "".join(stk[-part_length:]) == part:
                for i in range(part_length):
                    stk.pop()

        return "".join(stk)
