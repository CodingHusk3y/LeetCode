class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        letter = ""
        ptr1 = 0
        ptr2 = 0
        n1 = len(word1)
        n2 = len(word2)
        while ptr1 in range(n1) and ptr2 in range(n2):
            letter += word1[ptr1] + word2[ptr2]
            ptr1 += 1
            ptr2 += 1
        
        while ptr1 in range(ptr1, n1):
            letter += word1[ptr1]
            ptr1 += 1
        
        while ptr2 in range(ptr2, n2):
            letter += word2[ptr2]
            ptr2 += 1

        return letter
    

           
