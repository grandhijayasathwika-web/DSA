from collections import defaultdict 
class Solution(object):
    def smallestSubsequence(self, s):
        """
        :type s: str
        :rtype: str
        """
        freq=defaultdict(int)
        for c in s:
            freq[c]+=1
        se=set()
        ans=[]
        for c in s:
            freq[c]-=1
            if c in se:
                continue
            while ans and ans[-1]>c and freq[ans[-1]]>0:
                se.remove(ans.pop())
            ans+=c
            se.add(c)

            
        return ''.join(ans)
            
            
            
        