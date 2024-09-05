class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        radiant = deque()
        dire = deque()
        
        for i, senator in enumerate(senate):
            if senator == "R":
                radiant.append(i)
            else:
                dire.append(i) 

        while radiant and dire:
            r = radiant.popleft()
            d = dire.popleft()

            if r < d:
                radiant.append(r + len(senate))
            else:
                dire.append(d + len(senate))

        return "Radiant" if radiant else "Dire"