class Solution(object):
    def numberOfSpecialChars(self, word):
        """
        :type word: str
        :rtype: int
        """
        first_upper={}
        last_lower={}
        for i,c in enumerate(word):
            if c.islower():
                last_lower[c]=i
            else:
                first_upper.setdefault(c.lower(),i)
        count=0
        for ch in last_lower:
            if ch in first_upper and last_lower[ch]<first_upper[ch]:
                count+=1
        return count
        