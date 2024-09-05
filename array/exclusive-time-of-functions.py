class Solution:
    def exclusiveTime(self, n: int, logs: List[str]) -> List[int]:
        times = [0] * n
        stack = []
        start_times = {}

        # Parse logs and sort by timestamp
        parsed_logs = []
        for log in logs:
            id, flag, timestamp = log.split(':')
            parsed_logs.append((int(id), flag, int(timestamp)))
        parsed_logs.sort(key=lambda x: x[2])

        for i in range(len(parsed_logs)):
            id, flag, timestamp = parsed_logs[i]

            if flag == 'start':
                if stack:
                    # Add the exclusive time of the previous function to its time
                    times[stack[-1]] += timestamp - start_times[stack[-1]]
                stack.append(id)
                start_times[id] = timestamp
            else:
                # Add the execution time to the current function's time
                times[id] += timestamp - start_times[id] + 1
                stack.pop()
                if stack:
                    # Subtract the execution time from the next function's time
                    start_times[stack[-1]] = timestamp + 1

        return times