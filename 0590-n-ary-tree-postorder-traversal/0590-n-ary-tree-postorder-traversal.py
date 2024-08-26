"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        if not root:
            return []
        res = []
        st = [root]
        while st:
            r = st[-1]
            while r.children:
                st.append(r.children[0])
                ne = r.children[0]
                r.children.pop(0)
                r = ne
            res.append(st.pop().val)
        return res