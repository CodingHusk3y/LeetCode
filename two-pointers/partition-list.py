# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        smallHead = ListNode(0)
        bigHead = ListNode(0)

        smaller = smallHead
        bigger = bigHead

        current = head

        while current:
            if current.val < x:
                smaller.next = current
                smaller = smaller.next
            else:
                bigger.next = current
                bigger = bigger.next

            current = current.next

        bigger.next = None
        smaller.next = bigHead.next

        return smallHead.next