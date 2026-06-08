class Solution(object):
    def pivotArray(self, nums, pivot):
        """
        :type nums: List[int]
        :type pivot: int
        :rtype: List[int]
        """
        g,l,co=[],[],[]
        ans=[]
        for e in nums:
            if e>pivot:
                g.append(e)
            if e<pivot:
                l.append(e)
            if e==pivot:
                co.append(e)
        l.extend(co)
        l.extend(g)
        return l
