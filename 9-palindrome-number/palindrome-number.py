class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        l=str(x)
        y=l[::-1]
        return l==y
        