# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
        before_a = list1
        for i in range(a - 1):
            before_a = before_a.next

        after_b = before_a.next

        for j in range(b - a + 1):
            after_b = after_b.next

        before_a.next = list2
        while list2.next:
            list2 = list2.next

        list2.next = after_b

        return list1


        
        