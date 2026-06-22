class Solution(object):
    def maxNumberOfBalloons(self, text):
        """
        :type text: str
        :rtype: int
        """
        d={}
        for i in text:
            if i in 'balon':
                d[i]=d.get(i,0)+1
               
        return min(d.get('b',0),
                    d.get('a',0),d.get('l',0)//2,d.get('o',0)//2,d.get('n',0),)
        
        