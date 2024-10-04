class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        process = [0]*26

        for t in tasks:
            process[ord(t) - ord("A")] += 1

        process.sort()
        chunk = process[25] - 1
        max_idle = chunk * n

        for i in range(24, -1, -1):
            max_idle -= min(chunk, process[i])

        return len(tasks) + max_idle if max_idle >= 0 else len(tasks)