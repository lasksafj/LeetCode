# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def doubleIt(self, head: Optional[ListNode]) -> Optional[ListNode]:
        a = head
        A = [0]
        while a:
            A.append(a.val)
            a = a.next
        # print(A)
        carry = 0
        for i in range(len(A)-1, -1, -1):
            v = A[i]*2 + carry
            carry = v//10
            A[i] = v%10
        # print(A)
        a = None
        for n in A[::-1]:
            a = ListNode(n, a)
        return a if a.val > 0 else a.next