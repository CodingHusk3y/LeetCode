class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        ans = []
        for i in range(1, n+1):
            if i%3 == 0 and i%5 == 0:
                i = "FizzBuzz"
            elif i%3 == 0:
                i = 'Fizz'
            elif i%5 == 0:
                i = 'Buzz'
            else:
                i = f'{i}'
            ans.append(i)
        return ans
            
            

