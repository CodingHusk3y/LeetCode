class Solution:
    def chalkReplacer(self, chalk: List[int], k: int) -> int:
        remaining_in_last_round = k % sum(chalk)

        for i in range(len(chalk)):
            remaining_in_last_round -= chalk[i]

            if remaining_in_last_round < 0:
                return i

                