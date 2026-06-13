class Solution(object):
    def mapWordWeights(self, words, weights):
        """
        :type words: List[str]
        :type weights: List[int]
        :rtype: str
        """
        word=''
        for i in words:
            sum=0
            for c in i:
                sum+=weights[ord(c)-ord('a')]
            word+=chr((ord('z')-sum%26))
        return word


        