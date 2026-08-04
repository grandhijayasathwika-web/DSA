class Solution(object):
    def findMissingElements(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        set1=set(nums)
        mini=min(nums)
        maxi=max(nums)
        l=[i for i in range(mini,maxi+1)]
        set2=set(l)
        return list(sorted(set2 - set1))


        