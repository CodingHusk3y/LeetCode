class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = ['a', 'e', 'i', 'o', 'u']
        max_v = 0
        v_count = 0
        l = 0
        r = l + k

        for i in s[l:r]:
            if i in vowels:
                v_count += 1
        max_v = v_count

        l += 1
        r += 1

        while r <= len(s):
            if s[l - 1] in vowels:
                v_count -= 1
            if r-1 < len(s) and s[r-1] in vowels:
                v_count += 1

            max_v = max(max_v, v_count)

            l += 1
            r += 1

        return max_v
                    