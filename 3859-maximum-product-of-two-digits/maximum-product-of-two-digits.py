class Solution(object):
    def maxProduct(self, n):
        """
        :type n: int
        :rtype: int
        """
        l=list(str(n))
        max1=max(l)
        l.remove(max1)
        max2=max(l)
        ans=int(max1)*int(max2)
        return ans

        