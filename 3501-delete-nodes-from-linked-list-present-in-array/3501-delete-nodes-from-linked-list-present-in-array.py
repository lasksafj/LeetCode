# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def modifiedList(self, nums: List[int], head: Optional[ListNode]) -> Optional[ListNode]:
        nums = set(nums)
        h = head
        p = pp = ListNode(0, head)
        while h:
            if h.val in nums:
                p.next = h.next
            else:
                p = p.next
            h = h.next
        return pp.next