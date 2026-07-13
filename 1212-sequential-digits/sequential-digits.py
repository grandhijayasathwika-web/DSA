class Solution(object):
    def sequentialDigits(self, low, high):
        """
        :type low: int
        :type high: int
        :rtype: List[int]
        """
        ans=[]
        s='123456789'
        l=str(low)
        h=str(high)
        for le in range(len(l),len(h)+1):
            for st in range(0,10-le):
                num=int(s[st:st+le])
                if low<=num<=high:
                    ans.append(num)
        return ans


        