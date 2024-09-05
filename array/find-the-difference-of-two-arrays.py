class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        set1 = set(nums1)
        set2 = set(nums2)
        onlynums1 = set1 - set2
        onlynums2 = set2 - set1
        return [list(onlynums1), list(onlynums2)]
                
                    
