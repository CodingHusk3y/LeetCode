class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        preMap = defaultdict(list)
        for crs, pre in prerequisites:
            preMap[crs].append(pre)

        ans = []
        visited = set()
        circle = set()

        def dfs(course):
            if course in circle:
                return False
            if course in visited:
                return True

            circle.add(course)
            for preq in preMap[course]:
                if not dfs(preq):
                    return False

            circle.remove(course)
            visited.add(course)
            ans.append(course)
            return True

        for crs in range(numCourses):
            if not dfs(crs):
                return []

        return ans

        