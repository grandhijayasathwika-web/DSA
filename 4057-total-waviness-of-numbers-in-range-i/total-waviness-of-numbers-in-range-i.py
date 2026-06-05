class Solution(object):
    def totalWaviness(self, num1, num2):
        """
        :type num1: int
        :type num2: int
        :rtype: int
        """
        def waviness(n):
            s=str(n)
            su=0
            for i in range(1,len(s)-1):
                if s[i-1]>s[i]<s[i+1] or s[i-1]<s[i]>s[i+1]:
                    su+=1
            return su
        sum=0
        for i in range(num1,num2+1):
            sum+=waviness(i)
        return sum
        