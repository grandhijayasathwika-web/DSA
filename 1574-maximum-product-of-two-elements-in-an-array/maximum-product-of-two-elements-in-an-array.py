class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        maxi=max(nums)
        nums.remove(maxi)
        mai=max(nums)
        return (maxi-1)*(mai-1)
        