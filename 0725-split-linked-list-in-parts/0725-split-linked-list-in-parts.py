# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        n = 0
        A = []
        while head:
            A.append(head)
            head = head.next
        res = []
        if len(A) < k:
            for a in A:
                a.next = None
                res.append(a)
            for _ in range(k-len(A)):
                res.append(None)
        else:
            d = len(A)//k
            m = len(A)%k
            i = 0
            while i < len(A):
                res.append(A[i])
                A[i + d + (m>0) - 1].next = None
                i += d + (m>0)
                m -= 1
        return res