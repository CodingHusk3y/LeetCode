class Solution:
    def shiftingLetters(self, s: str, shifts: List[int]) -> str:
        shift_sum = sum(shifts)
        ans = ""
        for i in range(len(shifts)):
            shift_count = shift_sum % 26
            ans = ans + chr(97+shift_count+(ord(s[i])%97))
            shift_sum -= shifts[i]
        return ans

