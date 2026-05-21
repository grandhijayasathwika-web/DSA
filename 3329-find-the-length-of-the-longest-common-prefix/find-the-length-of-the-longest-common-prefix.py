class Solution(object):
    def longestCommonPrefix(self, arr1, arr2):
        """
        :type arr1: List[int]
        :type arr2: List[int]
        :rtype: int
        """
        arr1set=set()
        for val in arr1:
            while val not in arr1set and val>0:
                arr1set.add(val)
                val//=10
        longp=0
        for var in arr2:
            while var not in arr1set and var>0:
                var//=10
            if var>0:
                longp=max(longp,len(str(var)))
        return longp
        