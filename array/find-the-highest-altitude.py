class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        current = 0
        highest = current
        for attitude in gain:
            current += attitude
            highest = max(highest, current)

        return highest
        