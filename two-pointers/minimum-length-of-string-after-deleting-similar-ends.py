class Solution:
    def minimumLength(self, s: str) -> int:
        ptr1 = 0
        ptr2 = len(s) - 1
        while ptr1 < ptr2 and s[ptr1] == s[ptr2]:
            char = s[ptr1]
            while ptr1 <= ptr2 and s[ptr1] == char:
                ptr1 += 1
            while ptr1 <= ptr2 and s[ptr2] == char:
                ptr2 -= 1

        return ptr2 - ptr1 +1
            
