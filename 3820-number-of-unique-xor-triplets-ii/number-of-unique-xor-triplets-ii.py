class Solution(object):
    def uniqueXorTriplets(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        s=list(set(nums))
        pairs=set()
        for i in range(len(s)):
            for j in range(i,len(s)):
                pairs.add(s[i]^s[j])
        ans=set()
        for i in pairs:
            for j in s:
                ans.add(i^j)
        return len(ans)