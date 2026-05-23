class Solution(object):
    def check(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        sort_nums=sorted(nums)
        n=len(nums)
        for _ in range(len(nums)):
            arr=[0]*len(nums)
            for j in range (1,len(nums)):
                
                arr[j-1]=nums[j]
            arr[n-1]=nums[0]
            if arr==sort_nums:
                return True
            nums=arr

        return False



