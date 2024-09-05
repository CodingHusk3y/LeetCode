class Solution:
    def average(self, salary: List[int]) -> float:
        salary.sort()
        a = max(salary)
        b = min(salary)
        return (sum(salary) - a -b) / (len(salary)-2)