class Solution:
    def getEncryptedString(self, s: str, k: int) -> str:
        ans = []
        
        for i in range(len(s)):
            ans.append(s[(i + k) % len(s)])

        return ''.join(ans)