class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        stk = []
        ptr = 0
        
        for num in pushed:
            stk.append(num)

            while stk and stk[-1] == popped[ptr]:
                stk.pop()
                ptr += 1

        return not stk
            