class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        ans = [0] * n  # Initialize a list of zeros to store results
        stack = []  # Use a stack to track indices of temperatures

        for i in range(n):
            while stack and temperatures[i] > temperatures[stack[-1]]:
                # Update the result for days in the stack
                idx = stack.pop()
                ans[idx] = i - idx

            # Push the current day's index onto the stack
            stack.append(i)

        return ans
