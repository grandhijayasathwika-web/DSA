class Solution(object):
    def findGCD(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        def gcd(a,b):
            while b!=0:
                a,b=b,a%b
            return a
        maxi=max(nums)
        mini=min(nums)
        return gcd(maxi,mini)

        