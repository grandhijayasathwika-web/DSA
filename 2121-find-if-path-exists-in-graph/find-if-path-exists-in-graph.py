class Solution(object):
    def validPath(self, n, edges, source, destination):
        """
        :type n: int
        :type edges: List[List[int]]
        :type source: int
        :type destination: int
        :rtype: bool
        """
        s=set()
        neig=defaultdict(list)
        for n1,n2 in edges:
            neig[n1].append(n2)
            neig[n2].append(n1)
        def dfs(node,end,s):
            if node==end:
                return True
            if node in s:
                return False
            s.add(node)
            for n in neig[node]:
                if dfs(n,end,s):
                    return True
            return False
        return dfs(source, destination,s)