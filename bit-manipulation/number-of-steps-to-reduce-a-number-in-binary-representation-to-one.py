class Solution:
    def numSteps(self, s: str) -> int:
        number = int(s, 2)
        steps = 0
        
        while number > 1:
            if number % 2 == 0:
                number //= 2
            else:
                number += 1
            
            steps += 1

        return steps