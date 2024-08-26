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
            r = st.pop()
            res.append(r.val)
            for ne in r.children:
                st.append(ne)
            
        return res[::-1]