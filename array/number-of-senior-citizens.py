class Solution:
    def countSeniors(self, details: List[str]) -> int:
        start = 11
        end = start + 2
        count = 0

        for detail in details:
            if int(detail[start:end]) > 60:
                count += 1

        return count

