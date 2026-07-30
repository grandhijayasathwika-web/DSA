class Solution(object):
    def minimumPushes(self, word):
        """
        :type word: str
        :rtype: int
        """
        n=len(word)
        
        if n<=8:
            return n
        i=1
        sum=8
        while n>0:
            n-=8
            if n>8:
                sum+=8*(i+1)
                i=i+1
            elif n>0:
                sum+=n*(i+1)
                i+=1

            
        return sum
        