from collections import Counter
class Solution(object):
    def minimumPushes(self, word):
        """
        :type word: str
        :rtype: int
        """
        count=Counter(word)
        sortee=sorted(count.items(),key=lambda x:x[1],reverse=True)
        x,y=0,1
        n=1
        sum=0
        for i,j in sortee:
            x+=1
            if x<=8*n:
                sum+=j*y
                if x==8*n:
                    y+=1
                    n+=1
        return sum
                    


            


        