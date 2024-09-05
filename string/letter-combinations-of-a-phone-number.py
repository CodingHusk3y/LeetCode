class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []

        phone = {
            '2': "abc", '3': "def", '4': "ghi", '5': "jkl", 
            '6': "mno", '7': "pqrs", '8': "tuv", '9': "wxyz"
        }
        ans = []
        combi = []
        
        def backtrack(index):
            if len(combi) == len(digits):
                ans.append("".join(combi))
                return 
            current = digits[index]
            for char in phone[current]:
                combi.append(char)
                backtrack(index + 1)
                combi.pop()

        backtrack(0)
        return ans