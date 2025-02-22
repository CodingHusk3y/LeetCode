class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        ptr1 = 0
        ptr2 = len(numbers) - 1

        while ptr1 < ptr2:
            curr_sum = numbers[ptr1] + numbers[ptr2]
            if numbers[ptr1] + numbers[ptr2] > target:
                ptr2 -= 1
            elif curr_sum < target:
                ptr1 += 1
            else:
                return [ptr1 + 1, ptr2 + 1]

        
            
            