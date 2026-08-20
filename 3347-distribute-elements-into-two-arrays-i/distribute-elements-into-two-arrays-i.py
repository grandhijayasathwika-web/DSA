class Solution(object):
    def resultArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        arr1=[nums[0]]
        arr2=[nums[1]]
        x,y=nums[0],nums[1]
        n=len(nums)
        for i in range(2,n):
            if x>y:
                arr1.append(nums[i])
                x=nums[i]
            else:
                arr2.append(nums[i])
                y=nums[i]        
         
        arr1.extend(arr2)
        return arr1

        