class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        result = ""
        ptr1, ptr2 = 0, 0
        n = len(word1)
        m = len(word2)

        while ptr1 < n or ptr2 < m:
            if ptr1 < n:
                result += word1[ptr1]
                ptr1 += 1
            if ptr2 < m:
                result +=  word2[ptr2]
                ptr2 += 1

        return result        
