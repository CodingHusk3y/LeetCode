class Solution:
    def numEquivDominoPairs(self, dominoes: List[List[int]]) -> int:
        counting = defaultdict(int)

        for pair in dominoes:
            key = tuple(sorted(pair))
            counting[key] += 1

        return sum(count * (count - 1)) // 2 for count in counting.values()

