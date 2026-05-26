class Solution(object):
    def numberOfSpecialChars(self, word):
        """
        :type word: str
        :rtype: int
        """
        low=set()
        upp=set()
        for c in word:
            if c.islower():
                low.add(c)
            else:
                upp.add(c.lower())
        return len(low&upp)
