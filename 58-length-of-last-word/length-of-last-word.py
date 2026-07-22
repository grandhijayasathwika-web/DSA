class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        y=s.strip().split(' ')
        return len(y[-1])

        
        