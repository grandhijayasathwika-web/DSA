from collections import Counter
class Solution(object):
    def smallestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        count=Counter(s)
        left=[]
        middle=''
        for car in sorted(count):
            left.append(car*(count[car]//2))
            if count[car]%2==1:
                middle=car
        left=''.join(left)
        return left+middle+left[::-1]