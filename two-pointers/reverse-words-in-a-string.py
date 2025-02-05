class Solution:
    def reverseWords(self, s: str) -> str:
        ans = []
        ptr1 = 0
        ptr2 = 0
        n = len(s)

        while ptr2 < n:
            # Move ptr1 to the first non-space character
            while ptr1 < n and s[ptr1] == " ":
                ptr1 += 1
            
            # If ptr1 reaches the end, break
            if ptr1 >= n:
                break

            ptr2 = ptr1  # Start ptr2 at the first character of the word
            
            # Move ptr2 to the end of the current word
            while ptr2 < n and s[ptr2] != " ":
                ptr2 += 1

            # Extract the word and add to the list
            ans.append(s[ptr1:ptr2])

            # Move ptr1 to the next word
            ptr1 = ptr2

        return " ".join(ans[::-1])