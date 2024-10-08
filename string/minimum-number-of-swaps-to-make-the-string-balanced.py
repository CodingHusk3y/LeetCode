class Solution:
    def minSwaps(self, s: str) -> int:
        max_diff = 0
        diff = 0

        for char in s:
            if char == "]":
                diff += 1
            else:
                diff -= 1

            max_diff = max(max_diff, diff)

        return (max_diff + 1) // 2