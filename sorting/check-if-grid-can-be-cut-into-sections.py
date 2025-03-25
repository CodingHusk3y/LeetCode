class Solution:
    def checkValidCuts(self, n: int, rectangles: List[List[int]]) -> bool:
        x = sorted((r[0], r[2]) for r in rectangles)
        y = sorted((r[1], r[3]) for r in rectangles)

        def count_interval(intervals):
            prev_end = -1
            count = 0

            for start, end in intervals:
                if prev_end <= start:
                    count += 1
                prev_end = max(prev_end, end)
            
            return count
        
        return count_interval(x) >= 3 or count_interval(y) >= 3