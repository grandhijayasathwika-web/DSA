class Solution(object):
    def processStr(self, s):
        """
        :type s: str
        :rtype: str
        """
        a=[]
        for c in s:
            if c=='*'        :
                if a:
                    a.pop()
            elif c=='#':
                a.extend(a[:])
            elif c=='%':
                a.reverse()
            else: a.append(c)
        return ''.join(a)