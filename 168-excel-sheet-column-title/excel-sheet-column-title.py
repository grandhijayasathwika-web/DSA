class Solution(object):
    def convertToTitle(self, columnNumber):
        """
        :type columnNumber: int
        :rtype: str
        """

        x=columnNumber
        ans=''
        i=1
        while x>0: 
            i=(x-1)%26
            ans=chr(i+ord('A'))+ans
            x=(x-1)//26
        return ans

        