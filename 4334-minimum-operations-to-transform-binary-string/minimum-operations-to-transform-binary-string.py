class Solution(object):
    def minOperations(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: int
        """
        if s1=='1' and s2=='0':
            return -1
        s=list(s1)
        n=len(s)
        res=0
        for i in range(n):
            if s[i]==s2[i]:continue
            res+=1
            if s[i]=='1':
                if i==n-1:
                    res+=1
                else:
                    res+=s[i+1]=='0'
                    s[i+1]='0'
        return res

        