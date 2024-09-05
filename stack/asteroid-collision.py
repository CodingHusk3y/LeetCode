class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        # have a stk
        stk = []
        # loop over the array 
        # find another asteroid 
        for i in asteroids:
            # Check if go in the same direction with the asteroid in the top of the stk
            # if the same direction: push into the stk
            if i > 0:
                stk.append(i)
                continue
            # not the same direction: delete whichever have smaller absolute value
            while stk and 0 < stk[-1] < -i:
                stk.pop()
            if stk and 0 < stk[-1]:
                if stk[-1] == -i:
                    stk.pop()
                continue
            stk.append(i)    
        # return stk
        return stk 

