class Solution(object):
    def earliestFinishTime(self, landStartTime, landDuration, waterStartTime, waterDuration):
        """
        :type landStartTime: List[int]
        :type landDuration: List[int]
        :type waterStartTime: List[int]
        :type waterDuration: List[int]
        :rtype: int
        """
        def fun(start1,duration1,start2,duration2):
            fin=float('inf')
            for i in range(len(start1)):
                fin=min(fin,start1[i]+duration1[i])
            fin1=float('inf')
            for i in range(len(start2)):
                fin1=min(fin1,max(start2[i],fin)+duration2[i])
            return fin1
        a=fun(landStartTime, landDuration, waterStartTime, waterDuration)
        b=fun(waterStartTime, waterDuration,landStartTime, landDuration)
        return min(a,b)
        
    