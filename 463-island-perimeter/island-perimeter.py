class Solution(object):
    def islandPerimeter(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        count=0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]:
                    count+=4
                    if i  and grid[i-1][j] :
                        count-=2
                    if j and grid[i][j-1]:
                        count-=2
                #
        return count

        