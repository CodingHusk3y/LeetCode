class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        elements = Counter(nums)

        return [item[0] for item in elements.most_common(k)]