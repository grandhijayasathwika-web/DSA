class Solution(object):
    def maxTotalValue(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        m1=min(nums)
        m2=max(nums)
        return(m2-m1)*k