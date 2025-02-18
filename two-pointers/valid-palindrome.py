class Solution:
    def isPalindrome(self, s: str) -> bool:
        filtered = "".join(c.lower() for c in s if c.isalnum())
        ptr1 = 0
        ptr2 = len(filtered) - 1

        while ptr1 < ptr2:
            if filtered[ptr1] != filtered[ptr2]:
                return False
            
            ptr1 += 1
            ptr2 -= 1

        return True