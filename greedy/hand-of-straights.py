class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        n = len(hand)

        if n % groupSize != 0:
            return False

        count = Counter(hand)

        min_heap = list(count.keys())
        heapq.heapify(min_heap)

        while min_heap:
            current = min_heap[0]
            for i in range(groupSize):
                if count[current + i] == 0:
                    return False
                count[current + i] -= 1
                if count[current + i] == 0:
                    if current + i != heapq.heappop(min_heap):
                        return False

        return True