class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        s=dict()
        x=0
        for i,j in enumerate(nums):
            x=target-j
            if x in s:
                return [s[x],i]
            else:
                s[j]=i
        return -1

        