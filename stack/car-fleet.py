class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = sorted(zip(position, speed), reverse=True)
        stk = []

        for pos, spd in cars:
            time = (target - pos) / spd
            
            if not stk or time > stk[-1]:
                stk.append(time)

        return len(stk) 