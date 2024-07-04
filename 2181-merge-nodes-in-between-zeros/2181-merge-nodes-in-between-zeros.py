# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        cur = head
        s = 0
        prev = ListNode(0)
        while cur:
            if cur.val == 0:
                cur.val = s
                prev.next = cur
                prev = cur
                s = 0
            else:
                s += cur.val
            cur = cur.next
        return head.next