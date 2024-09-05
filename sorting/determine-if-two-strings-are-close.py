class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        if not word1 or not word2:
            return False

        if len(word1) != len(word2):
            return False

        dict1 = {}
        dict2 = {}

        for i in word1:
            if i not in dict1:
                dict1[i] = 1
            else:
                dict1[i] += 1

        for j in word2:
            if j not in dict2:
                dict2[j] = 1
            else:
                dict2[j] += 1

        if set(dict1.keys()) != set(dict2.keys()):
            return False

        if sorted(dict1.values()) != sorted(dict2.values()):
            return False

        return True
        
