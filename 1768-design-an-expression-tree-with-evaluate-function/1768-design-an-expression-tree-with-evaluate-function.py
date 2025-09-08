import abc 
from abc import ABC, abstractmethod 
"""
This is the interface for the expression tree Node.
You should not remove it, and you can define some classes to implement it.
"""
op = {
    '+': lambda a, b: a + b,
    '-': lambda a, b: a - b,
    '*': lambda a, b: a * b,
    '/': lambda a, b: a // b,
}
class Node(ABC):
    @abstractmethod
    # define your fields here
    def evaluate(self) -> int:
        pass

class TreeNode(Node):
    def __init__(self, val, left=None,right=None):
        self.val = val
        self.left = left
        self.right = right
    def evaluate(self):
        if self.val not in op:
            return self.val
        return op[self.val](self.left.evaluate(), self.right.evaluate())

"""    
This is the TreeBuilder class.
You can treat it as the driver code that takes the postinfix input
and returns the expression tree representing it as a Node.
"""

class TreeBuilder(object):
    def buildTree(self, postfix: List[str]) -> 'Node':
        st = []
        for s in postfix:
            if s in op:
                b = st.pop()
                a = st.pop()
                st.append(TreeNode(s, a, b))
            else:
                st.append(TreeNode(int(s)))
        return st[0]
		
"""
Your TreeBuilder object will be instantiated and called as such:
obj = TreeBuilder();
expTree = obj.buildTree(postfix);
ans = expTree.evaluate();
"""
        