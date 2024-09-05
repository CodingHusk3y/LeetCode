class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        occ_count = {}
        l = 0
        max_count = 0
        maxf = 0

        for r in range(len(s)):
            occ_count[s[r]] = 1 + occ_count.get(s[r], 0)
            maxf = max(maxf, occ_count[s[r]])
            
            while (r - l + 1) - maxf > k:
                occ_count[s[l]] -= 1
                l += 1
            
            max_count = max(max_count, r - l + 1)

        return max_count