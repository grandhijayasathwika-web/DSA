class Solution(object):
    def minimumSwaps(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count=0
        end=len(nums)-1
        for i in range(len(nums)):
            if nums[i]==0 :count+=1
        ans=0
        while count:
            count-=1
            
            if nums[end]==0:
                end-=1
                continue
            else:
                ans+=1
           
            end-=1


        return ans
        