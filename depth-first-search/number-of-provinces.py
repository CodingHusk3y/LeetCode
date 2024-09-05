class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        visited = set()
        ans = 0

        def dfs(start):
            # Visit the start node and all its connected nodes
            visited.add(start)
            for end in range(len(isConnected)):
                if isConnected[start][end] == 1 and end not in visited:
                    dfs(end)
        
        # Iterate through all nodes
        for i in range(len(isConnected)):
            if i not in visited:
                dfs(i)  # Start a new DFS if the node is not visited
                ans += 1  # Increment the count of connected components

        return ans
