class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = {'u', 'e', 'o', 'a', 'i', 'U', 'E', 'O', 'A', 'I'}
        s1 = list(s)
        left = 0 
        right = len(s) - 1
        while left < right:
            if s1[left] not in vowels:
                left += 1
            elif s1[right] not in vowels:
                right -= 1
            else:   
                s1[left], s1[right] = s1[right], s1[left]
                left += 1
                right -= 1
        return "".join(s1) 


