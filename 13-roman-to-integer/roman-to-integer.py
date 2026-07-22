class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        di=    {'I'      :       1,
            'V' :            5,
            'X':            10,
            'L' :            50,
            'C' :             100,
            'D'  :           500,
            'M' :            1000,}
        sum=0
        var={ 'IV':4,'IX':9,'XL':40,'XC':90,'CD':400,'CM':900}
        for i in range(len(s)-1):
            if di[s[i]]<di[s[i+1]]:
                sum-=di[s[i]]
            else:
                sum+=di[s[i]]
        sum+=di[s[-1]]
        return sum

        
        