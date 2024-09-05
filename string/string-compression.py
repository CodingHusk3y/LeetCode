class Solution:
    def compress(self, chars: List[str]) -> int:
        ptr1 = 0
        ptr2 = ptr1 + 1
        count = 1
        for ptr2 in range(1, len(chars) + 1):
            if ptr2 < len(chars) and chars[ptr1] == chars[ptr2]:
                count += 1
            else:
                if count > 1:
                    count_str = str(count)
                    chars[ptr1 + 1:ptr1 + 1 + len(count_str)] = count_str
                    ptr1 += len(count_str)
                ptr1 += 1
                if ptr2 < len(chars):  # Update character
                    chars[ptr1] = chars[ptr2]
                count = 1 
        
        return len(chars[:ptr1])


