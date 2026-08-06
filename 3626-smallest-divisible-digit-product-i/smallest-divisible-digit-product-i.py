class Solution(object):
    def smallestNumber(self, n, t):
        """
        :type n: int
        :type t: int
        :rtype: int
        """
        def ceck(n):
            x=1
            y=n
            while n>0:
                x*=(n%10)
                n//=10
                if n==0: break
            return x%t==0
        while not ceck(n):
            n+=1
        return n
        
        
        
