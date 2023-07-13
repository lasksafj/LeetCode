# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if head.next == None:
            return
        a,b = head,head
        prev_a = None
        while b and b.next:
            prev_a = a
            a = a.next
            b = b.next.next
        prev_a.next = None
        l,r = None,a.next
        while a:
            a.next = l
            l = a
            a = r
            if r:
                r = r.next
        while head.next:
            head_r = head.next
            l_r = l.next
            head.next = l
            l.next = head_r
            head = head_r
            l = l_r
        head.next = l