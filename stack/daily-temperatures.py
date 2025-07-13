class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        ans = [0] * n
        stk = []

        for i, temp in enumerate(temperatures):
            while stk and temperatures[i] > temperatures[stk[-1]]:
                prev = stk.pop()
                ans[prev] = i - prev
            
            stk.append(i)

        return ans