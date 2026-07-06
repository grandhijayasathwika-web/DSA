class Solution(object):
    def removeCoveredIntervals(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: int
        """
        intervals.sort(key=lambda x:(x[0],-x[1]))
        count=0
        max_end=0
        for i,j in intervals:
            if j>max_end:
                count+=1
                max_end=j
        return count
        