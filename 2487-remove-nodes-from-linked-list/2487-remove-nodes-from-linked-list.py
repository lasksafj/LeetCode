# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        h = head
        m = [ListNode(inf, h)]
        while h:
            m.append(h)
            h = h.next
        ma = m[-1].val
        ne = m[-1]
        for i in range(len(m)-2,0,-1):
            if m[i].val < ma:
                m[i-1].next = ne
                m[i] = None
            else:
                ma = m[i].val
                ne = m[i]
        return m[0].next