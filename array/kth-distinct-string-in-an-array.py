class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        freq = defaultdict(int)
        for char in arr:
            freq[char] += 1

        distinct = []
        for key in freq:
            if freq[key] == 1:
                distinct.append(key)

        return distinct[k - 1] if len(distinct) >= k else ""
            
