# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def pairSum(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: int
        """
        a=[]
        n=0
        while head :
            a.append(head.val)
            n+=1
            head=head.next
        maxi=0
        for i in range(n//2):
            maxi=max(maxi,a[i]+a[n-1-i])
        return maxi


        