class Solution:
    def stringHash(self, s: str, k: int) -> str:
        n = len(s)
        res = ""

        table = {chr(i): i - ord('a') for i in range(ord('a'), ord('z') + 1)}

        for i in range(0, n, k):
            sub = s[i:i+k]
            total = sum(table[char] for char in sub)
            hashedChar = total % 26
            res += chr(hashedChar + ord('a'))

        return res