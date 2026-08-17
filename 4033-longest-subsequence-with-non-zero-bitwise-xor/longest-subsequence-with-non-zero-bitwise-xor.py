class Solution(object):
    def longestSubsequence(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # def x(a,b):
        #     return a^b
        x=0
        if len(set(nums))==1 and nums[0]==0:
            return 0
        n=len(nums)
        for i in range(len(nums)):
            x=x^nums[i]
        return n-1 if x==0 else n
        