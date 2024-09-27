class Solution:
    def shiftingLetters(self, s: str, shifts: List[int]) -> str:
        Counter = len(s)
        new_str = ""

        for i in range(len(s)):
            sum_count  = sum(shifts[ i : : ] )
            char = chr((ord(s[i]) - ord('a') + sum_count) % 26 + ord('a'))
            new_str = new_str + char
	    
        return new_str
