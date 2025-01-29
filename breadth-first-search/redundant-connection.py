class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        adj = [[] for i in range(len(edges) + 1)]

        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        visited = [False] * (n + 1)
        cycles = set()
        cycleStart = -1

        def dfs(node, parent):
            nonlocal cycleStart
            if visited[node]:
                cycleStart = node
                return True

            visited[node] = True

            for neighbor in adj[node]:
                if neighbor == parent:
                    continue
                if dfs(neighbor, node):
                    if cycleStart != -1:
                        cycles.add(neighbor)
                    if node == cycleStart:
                        cycleStart = -1

                    return True

            return False

        dfs(1, -1)

        for u, v in reversed(edges):
            if u in cycles and v in cycles:
                return [u, v]

        return []
        
