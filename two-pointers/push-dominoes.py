class Solution:
    def pushDominoes(self, dominoes: str) -> str:
        n = len(dominoes)
        forces = [0] * n

        force = 0
        for i in range(n):
            if dominoes[i] == "R":
                force += n
            elif dominoes[i] == "L":
                force = 0
            else:
                force = max(force - 1, 0) 
            forces[i] += force

        force = 0
        for i in range(n, -1, -1):
            if dominoes[i] == "L":
                force += n
            elif dominoes[i] == "R":
                force = 0
            else:
                force = max(force - 1, 0) 
            forces[i] -= force

        ans = []
        for push in forces:
            if push > 0:
                ans.append("R")
            elif push < 0:
                ans.append("L")
            else:
                ans.append(".")
        
        return "".join(ans)