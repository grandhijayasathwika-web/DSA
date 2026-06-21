class Solution(object):
    def maxIceCream(self, costs, coins):
        """
        :type costs: List[int]
        :type coins: int
        :rtype: int
        """
        costs.sort()
        ans=0
        for i in costs:
            if i<=coins:
                ans+=1
                coins-=i
            else:
                break
        return ans
        