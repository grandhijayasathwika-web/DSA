class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        x=len(needle)
        ans=-1
        y=len(haystack)
        if x==0:
            return 0
        for i in range(y-x+1):
            if haystack[i:i+x]==needle:
                return i
        return -1
        