# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        o,v = ListNode(0), ListNode(0)
        ho,hv = o,v
        cur = head
        i = 1
        while cur:
            if i%2:
                o.next = cur
                o = o.next
            else:
                v.next = cur
                v = v.next
            i += 1
            cur = cur.next
        o.next = hv.next
        v.next = None
        return head