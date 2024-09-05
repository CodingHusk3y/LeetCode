class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        potions.sort()
        ans = []
        for spell in spells:
            ans.append(self.FindNums(spell, potions, success))

        return ans

    def FindNums(self, num, arr, target):
        if num * arr[-1] < target:
            return 0

        left = 0
        right = len(arr) - 1

        while left <= right:
            mid = (left + right) // 2
            if num * arr[mid] >= target:
                right = mid - 1
            else:
                left = mid + 1

        return len(arr) - left 
            