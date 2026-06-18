class Solution(object):
    def angleClock(self, hour, minutes):
        """
        :type hour: int
        :type minutes: int
        :rtype: float
        """
        hourangle=(hour%12)*30+minutes*0.5
        minuteAngle=minutes*6
        ans=abs(hourangle-minuteAngle)
        return min(ans,360-ans)