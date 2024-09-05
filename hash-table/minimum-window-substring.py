class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if s == t:
            return s
        if not s or not t or len(s) < len(t):
            return ""
        
        need = collections.defaultdict(int)
        min_length = float('inf')
        min_start = 0
        start = 0
        count = 0

        for char in t:
            need[char] += 1

        for end in range(len(s)):
            if need[s[end]] > 0:
                count += 1
            need[s[end]] -= 1

            while count == len(t):
                if end - start + 1 < min_length:
                    min_length = end - start + 1
                    min_start = start

                need[s[start]] += 1
                if need[s[start]] > 0:
                    count -= 1
                start += 1

        if min_length == float('inf'):
            return ""

        return s[min_start: min_start + int(min_length)]

        



