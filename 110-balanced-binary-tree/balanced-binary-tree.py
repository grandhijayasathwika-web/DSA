# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isBalanced(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: bool
        """
        if not root:return True
        def fun(node):
            if not node:return 0
            left=fun(node.left)
            ri=fun(node.right)
            if left==-1 or ri==-1 or abs(left-ri)>1:return -1
            
            return 1+max(left,ri)
        return fun(root)!=-1
        