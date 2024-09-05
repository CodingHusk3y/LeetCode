class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        size = len(s1)
        count_s1 = Counter(s1)
        window_count = Counter()

        for right in range(len(s2)):
            window_count[s2[right]] += 1

            if right >= size:
                if window_count[s2[right - size]] == 1:
                    del window_count[s2[right - size]]
                else:
                    window_count[s2[right - size]] -= 1
        
            if window_count == count_s1: 
                return True

        return False



