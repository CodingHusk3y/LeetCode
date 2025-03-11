class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        freq = {'a': 0, 'b': 0, 'c': 0}
        left = 0
        ans = 0

        for right in range(len(s)):
            freq[s[right]] += 1

            while all(freq[i] > 0 for i in 'abc'):
                ans += len(s) - right
                freq[s[left]] -= 1
                left += 1

        return ans