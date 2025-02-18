class Solution:
    def smallestNumber(self, pattern: str) -> str:
        ans = []
        num_stk = []

        for i in range(len(pattern) + 1):
            num_stk.append(i + 1)

            if i == len(pattern) or pattern[i] == "I":
                while num_stk:
                    ans.append(str(num_stk.pop()))

        return "".join(ans)

