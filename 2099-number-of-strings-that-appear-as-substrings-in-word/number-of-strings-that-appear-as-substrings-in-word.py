class Solution(object):
    def numOfStrings(self, patterns, word):
        """
        :type patterns: List[str]
        :type word: str
        :rtype: int
        """
        ans=0
        for c in patterns:
            if word.find(c)!=-1:
                ans+=1
        return ans
        