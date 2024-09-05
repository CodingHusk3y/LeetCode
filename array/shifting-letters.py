class Solution:
    def shiftingLetters(self, s: str, shifts: List[int]) -> str:
        n = len(s)
        if n == 0: 
            return ""

        shift = 0
        ans = list(s)

        for i in range(n - 1, -1, -1):
            shift += shifts[i]

            ans[i] = chr((((ord(s[i]) - ord('a')) + shift) % 26) + ord('a')) 

        return ''.join(ans)
