
class Solution(object):
    mod=10**9+7
    def dfs(self,g,x,f):
        maxd=0
        for y in g[x]:
            if y==f:
                continue
            maxd=max(maxd,self.dfs(g,y,x)+1)
        return maxd
    def assignEdgeWeights(self, edges):
        """
        :type edges: List[List[int]]
        :rtype: int
        """
        adj=defaultdict(list)
        for i,j in edges:
            adj[i].append(j)
            adj[j].append(i)
        maxd=self.dfs(adj,1,0)
        return pow(2,maxd-1,self.mod)
