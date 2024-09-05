class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}

        for num in nums:
            if num in freq:
                freq[num] += 1
            else:
                freq[num] = 1

        sorted_desc = dict(sorted(freq.items(), key=lambda item: item[1], reverse=True))
        top_k = list(sorted_desc.keys())[:k]

        return top_k