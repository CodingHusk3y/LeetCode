class Solution:
    def decodeString(self, s: str) -> str:
        # maintain a stk of tasks
        num_stk = []
        str_stk = []
        curr_str = ""
        curr_num = 0

        for char in s:
            if char.isdigit():
                curr_num = curr_num * 10 + int(char)
            elif char == "[":
                num_stk.append(curr_num)
                str_stk.append(curr_str)
                curr_num = 0
                curr_str = ""
            elif char == "]":
                prev_str = str_stk.pop()
                repeat = num_stk.pop()
                curr_str = prev_str + curr_str * repeat
            else:
                curr_str += char

        return curr_str
        # whenever face a number of task, put that into the stk
        # if follow by the number is a string we will perform the task until we done with the number 
