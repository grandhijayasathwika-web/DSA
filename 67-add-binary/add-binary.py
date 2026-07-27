class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        c=[]
        i=len(a)-1
        j=len(b)-1
        carr=0
        while i>=0 or j>=0 or carr:
            if i>=0:
                carr+=int(a[i])
                i-=1
            if j>=0:
                carr+=int(b[j])
                j-=1
            c.append(str(carr%2))
            carr//=2
        return ''.join(reversed(c))
        