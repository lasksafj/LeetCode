# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:
        prev = ListNode(head.val)
        res = [inf,-inf]
        i = 0
        prev_i = -1
        l = -1
        while head.next:
            if (head.val > prev.val and head.val > head.next.val)\
            or (head.val < prev.val and head.val < head.next.val):
                if prev_i >= 0:
                    res[0] = min(res[0], i-prev_i)
                prev_i = i
                
                if l < 0:
                    l = i
                else:
                    res[1] = max(res[1], i-l)
            prev = head
            head = head.next
            i += 1
        if res[0] == inf:
            res[0] = -1
        if res[1] == -inf:
            res[1] = -1
        return res