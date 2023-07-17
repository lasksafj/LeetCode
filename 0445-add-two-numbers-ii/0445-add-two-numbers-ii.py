# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        def reverse(h):
            prev = None
            while h:
                ne = h.next
                h.next = prev
                prev = h
                h = ne
            return prev
        l1 = reverse(l1)
        l2 = reverse(l2)
        cur = ListNode(-1)
        h = cur
        carry = 0
        while l1 and l2:
            carry += l1.val + l2.val
            cur.next = ListNode(carry%10)
            carry //= 10
            cur = cur.next
            l1,l2 = l1.next,l2.next
        l = l1 if l1 else l2
        while l or carry > 0:
            carry += l.val if l else 0
            cur.next = ListNode(carry%10)
            carry //= 10
            cur = cur.next
            l = l.next if l else l
        return reverse(h.next)