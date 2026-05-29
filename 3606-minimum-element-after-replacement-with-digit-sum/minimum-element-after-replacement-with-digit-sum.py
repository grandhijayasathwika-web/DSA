class Solution(object):
    def minElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        def fun(a):
            summ=0
            while a>0:
                summ+=a%10
                a//=10
            return summ
        arr=[]
        for i in range(len(nums)):
            s=fun(nums[i])
            nums[i]=s
        return min(nums)

        

        