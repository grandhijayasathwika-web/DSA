from collections import defaultdict
class Solution(object):
    def maximumLengthSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        count=defaultdict(int)
        left=0
        res=0
        for ri,c in enumerate(s):
            count[c]+=1
            while count[c]>2:
                x=s[left]
                count[x]-=1
                left+=1
            res=max(res,ri-left+1)
        return res
        