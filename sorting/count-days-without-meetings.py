class Solution:
    def countDays(self, days: int, meetings: List[List[int]]) -> int:
        if not meetings:
            return days

        meetings.sort()
        merge = []

        for start, end in meetings:
            if merge and merge[-1][1] >= start:
                merge[-1][1] = max(merge[-1][1], end)
            else:
                merge.append([start, end])

        meeting_days = sum(end - start + 1 for start, end in merge)

        return days - meeting_days