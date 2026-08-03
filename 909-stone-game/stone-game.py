class Solution(object):
    def stoneGame(self, piles):
        """
        :type piles: List[int]
        :rtype: bool
        """
        n=len(piles)
        total=sum(piles)
        dp=[[-1]*n for _ in range(n)]
        def solve(i,j):
            if i>j: return 0
            if dp[i][j]!=-1:
                return dp[i][j]
            choose_i=piles[i]+min(solve(i+2,j),solve(i+1,j-1))
            choose_j=piles[j]+min(solve(i,j-2),solve(i+1,j-1))
            dp[i][j]= max(choose_i,choose_j)
            return dp[i][j]
        alex_score=solve(0,n-1)
        return alex_score>total//2



        