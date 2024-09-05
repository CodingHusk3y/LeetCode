class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        count = s.split()
        return len(count[-1])