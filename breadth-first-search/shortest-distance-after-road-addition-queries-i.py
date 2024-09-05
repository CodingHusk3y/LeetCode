class Solution:
    def shortestDistanceAfterQueries(self, n: int, queries: List[List[int]]) -> List[int]:
        # Initialize the graph with the default roads
        graph = [[] for _ in range(n)]
        for i in range(n - 1):
            graph[i].append((i + 1, 1))  # road from i to i+1 with distance 1
        
        def dijkstra() -> int:
            dist = [float('inf')] * n
            dist[0] = 0
            pq = [(0, 0)]  # (distance, city)
            
            while pq:
                current_dist, u = heapq.heappop(pq)
                
                if current_dist > dist[u]:
                    continue
                
                for v, length in graph[u]:
                    new_dist = current_dist + length
                    if new_dist < dist[v]:
                        dist[v] = new_dist
                        heapq.heappush(pq, (new_dist, v))
            
            return dist[n - 1]
        
        answer = []
        
        for ui, vi in queries:
            graph[ui].append((vi, 1))  # Add new road with distance 1
            shortest_path_length = dijkstra()
            answer.append(shortest_path_length)
        
        return answer