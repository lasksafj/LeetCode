# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
        dummy = ListNode(0, list1)
        cur = dummy
        while a > 0:
            cur = cur.next
            a -= 1
            b -= 1
        left = cur
        while a <= b:
            cur = cur.next
            b -= 1
        left.next = list2
        while list2.next:
            list2 = list2.next
        list2.next = cur.next
        return dummy.next