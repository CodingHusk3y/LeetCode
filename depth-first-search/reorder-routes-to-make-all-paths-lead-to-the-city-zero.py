class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        graph = defaultdict(list)

        for u, v in connections:
            graph[u].append((v, True))
            graph[v].append((u, False))

        def dfs(city, parent):
            reverse = 0
            for neighbor, away in graph[city]:
                if neighbor != parent:
                    if away:
                        reverse += 1

                    reverse += dfs(neighbor, city)

            return reverse

        return dfs(0, -1)
