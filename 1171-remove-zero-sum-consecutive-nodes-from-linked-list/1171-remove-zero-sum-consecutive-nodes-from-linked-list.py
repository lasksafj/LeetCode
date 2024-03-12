# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeZeroSumSublists(self, head: Optional[ListNode]) -> Optional[ListNode]:
        ret_head = ListNode(0, head)
        mp = {}
        mp[0] = ret_head
        A = [0]
        
        # (l,r]
        def remove(l,r):
            while l.next != r:
                l.next = l.next.next
                del mp[A[-1]]
                A.pop()
            l.next = l.next.next
        
        s = 0
        while head:
            s += head.val
            if s in mp:
                remove(mp[s], head)
            else:
                A.append(s)
                mp[s] = head
            head = head.next
        return ret_head.next