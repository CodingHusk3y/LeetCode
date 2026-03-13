class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # keep track of the occurance of each number
        # Sort the numbers by it's ocurance
        # get the k elements 
        tracking = {}

        for number in nums:
            if number in tracking:
                tracking[number] += 1
            else:
                tracking[number] = 1

        tracking = sorted(tracking.items(), key=lambda item: item[1], reverse=True)

        return [num for num, count in tracking[:k]]
        