from collections import deque
class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        n=len(prerequisites)
        adj=[[] for _ in range(numCourses)]
        for i,j in prerequisites:
            if i==j:
                return False
            adj[j].append(i)
            
        self.que=deque()
        self.visit=set()
        def bfs(node):
            self.que.clear()
            self.visit=set()

            self.que.append(node)
            self.visit.add(node)
            while self.que:
                n=self.que.popleft()
                for ngbr in adj[n]:
                    if ngbr==node:
                        return False
                    if ngbr not in self.visit:
                        self.visit.add(ngbr)
                        self.que.append(ngbr)
            return True
        for i in range(numCourses):
            if bfs(i)==False:
                return False
        return True




        