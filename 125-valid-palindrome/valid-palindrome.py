class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        st=''
        for ch in s:
            if not ch.isalnum():
                continue
            else:
                st+=ch.lower()
        return st==st[::-1]

        