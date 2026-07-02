from collections import deque
class Solution(object):
    def findSafeWalk(self, grid, health):
        """
        :type grid: List[List[int]]
        :type health: int
        :rtype: bool
        """
        dir=[[1,0],[0,1],[-1,0],[0,-1]]
        n=len(grid)
        m=len(grid[0])
        dis=[[float('inf')]*m for _ in range(n)]
        q=deque()
        q.append((0,0))
        dis[0][0]=grid[0][0]
        
        while q:
            x,y=q.popleft()
            if x==n-1 and y==m-1:
                return True
            for dx,dy in dir:
                nx,ny=dx+x,dy+y
                if nx<0 or ny<0 or nx>=n or ny>=m:
                    continue
                cost= dis[x][y]+grid[nx][ny]
                if cost>=health:
                    continue
                if cost<dis[nx][ny]:
                    dis[nx][ny]=cost
                    if grid[nx][ny]==0:
                        q.appendleft((nx,ny))
                    else:
                        q.append((nx,ny))
        return False


        