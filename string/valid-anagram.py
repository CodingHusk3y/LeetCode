class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        map_s = {}
        map_t = {}

        for i in s:
            if i in map_s:
                map_s[i] += 1
            else:
                map_s[i] = 1

        for j in t:
            if j in map_t:
                map_t[j] += 1
            else:
                map_t[j] = 1

        return map_s == map_t