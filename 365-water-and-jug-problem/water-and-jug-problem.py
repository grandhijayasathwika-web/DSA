class Solution(object):
    def canMeasureWater(self, x, y, target):
        """
        :type x: int
        :type y: int
        :type target: int
        :rtype: bool
        """
        def gcd(a,b):
            while b!=0:
                a,b=b,a%b
            return a
        a=gcd(x,y)
        if x+y<target:return False
        return target%a==0