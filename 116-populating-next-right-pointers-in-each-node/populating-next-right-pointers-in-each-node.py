from collections import deque
"""
# Definition for a Node.
class Node(object):
    def __init__(self, val=0, left=None, right=None, next=None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution(object):
    def connect(self, root):
        """
        :type root: Node
        :rtype: Node
        """
        if not root:
            return root
        ans=[]
        q=deque([root])
        while q:
            level=[]
            size=len(q)
            for _ in range(size):
                node=q.popleft()
                level.append(node)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            ans.append(level)
        for a in ans:
            n=len(a)
            for i in range(n-1):
                a[i].next=a[i+1]
            a[n-1].next=None

        return root
