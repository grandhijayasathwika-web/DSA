class Solution(object):
    def minScore(self, n, roads):
        """
        :type n: int
        :type roads: List[List[int]]
        :rtype: int
        """
        adj={}
        visit=set()
        
        ans=[float('inf')]
        for a,b,c in roads:
            if  a not in adj:
                adj[a]=[]
            if b not in adj :
                adj[b]=[]
            adj[a].append((b,c))
            adj[b].append((a,c))
        def dfs(i):
            
            visit.add(i)
            for k,j in adj[i]:
                ans[0] = min(ans[0], j)
                
                if k not in visit:
                    dfs(k)
        dfs(1)
        return ans[0]

