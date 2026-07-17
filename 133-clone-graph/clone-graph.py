from collections import deque

"""
# Definition for a Node.
class Node(object):
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution(object):
    def cloneGraph(self, node):
        """
        :type node: Node
        :rtype: Node
        """
        if not node:
            return node
        visited=set()
        que=deque([node])
        m={}
        while que:
            n=que.popleft()
            if n in visited:
                continue
            visited.add(n)
            if n not in m:
                m[n]=Node(n.val)
            for neigh in n.neighbors:
                if neigh not in m:
                    m[neigh]=Node(neigh.val)
                m[n].neighbors.append(m[neigh])
                que.append(neigh)
        return m[node]



        