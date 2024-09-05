class Solution:
    def firstPalindrome(self, words: List[str]) -> str:
        for i in words:
            ptr1 = 0
            ptr2 = len(i) - 1
            while ptr1 <= ptr2:
                if i[ptr1] == i[ptr2]:
                    ptr1 += 1
                    ptr2 -= 1
                else: 
                    break
            if ptr1 > ptr2:
                return i
        return ""