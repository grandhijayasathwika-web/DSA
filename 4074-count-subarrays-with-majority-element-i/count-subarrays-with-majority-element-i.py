class Solution(object):
    def countMajoritySubarrays(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        n=len(nums)
        ans=0
        for i in range(n):
            cnt=0
            for j in range(i,n):
                cnt +=1 if target==nums[j] else -1
                if cnt>0:
                    ans+=1
        return ans
