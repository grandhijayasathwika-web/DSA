class Solution(object):
    def maxActiveSectionsAfterTrade(self, s):
        n=len(s)
        count1=s.count('1')
        inactive_blocks=[]
        i=0
        while i<n:
            if s[i]=='0':
                start=i
                while i<n and s[i]=='0':
                    i+=1
                inactive_blocks.append(i-start)
            else:
                i+=1
        maxi=0
        for i in range(1,len(inactive_blocks)):
            maxi=max(maxi,inactive_blocks[i]+inactive_blocks[i-1])
        return maxi+count1
