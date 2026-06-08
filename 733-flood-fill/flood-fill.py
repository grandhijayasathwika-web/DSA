class Solution(object):
    def floodFill(self, image, sr, sc, color):
        """
        :type image: List[List[int]]
        :type sr: int
        :type sc: int
        :type color: int
        :rtype: List[List[int]]
        """
        clor=image[sr][sc]
        if image[sr][sc]==color:
            return image
        def dfs(r,c):
            if image[r][c]==clor:
                image[r][c]=color
                if r>0:
                    dfs(r-1,c)
                if r<len(image)-1:
                    dfs(r+1,c)
                if c>0:
                    dfs(r,c-1)
                if c<len(image[0])-1:
                    dfs(r,c+1)
        dfs(sr,sc)
        return image

        