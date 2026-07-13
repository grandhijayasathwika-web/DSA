class Solution(object):
    def pivotInteger(self, n):
        """
        :type n: int
        :rtype: int
        """
        summ=(n*(n+1))//2
        lsum=rsumm=0
        for i in range(1,n+1):
    
            lsum+=i
            rsumm=summ-lsum+i
            if lsum==rsumm:
                return i
            
            
        return -1
        