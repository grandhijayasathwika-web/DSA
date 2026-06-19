class Solution(object):
    def largestAltitude(self, gain):
        """
        :type gain: List[int]
        :rtype: int
        """
        a=[0]
        for i in gain:
            s=a[-1]+i
            a.append(s)
        return max(a)
        