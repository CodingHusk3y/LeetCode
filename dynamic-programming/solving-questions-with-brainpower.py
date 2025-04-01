class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        cache = [0] * len(questions)

        def backtrack(i):
            if i >= len(questions):
                return 0

            if cache[i]:
                return cache[i]

            point, skip = questions[i]
            cache[i] = max(
                backtrack(i + 1),
                point + backtrack(i + 1 + skip)
            )

            return cache[i]

        return backtrack(0)