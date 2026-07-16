
class Solution(object):
    def gcdSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        def gcd(a, b):
            while b != 0:
                a, b = b, a % b
            return a

        maxi=nums[0]
        n=len(nums)
        arr=[]
        arr.append(nums[0])
        for i in range(1,n):
            maxi=max(maxi,nums[i])
            arr.append(gcd(maxi,nums[i]))
           
        arr.sort()
        summ=0
        for i in range(n//2):
            summ+=gcd(arr[i],arr[n-1-i])
        return summ
        

        