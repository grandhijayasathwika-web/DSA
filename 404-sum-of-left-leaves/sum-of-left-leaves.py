# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def sumOfLeftLeaves(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        self.sum=0
        def fun(root):
        
            if not root:
                return 0
            if root.left:
                if root.left.left is None and root.left.right is None:
                    self.sum+=root.left.val
                fun(root.left)

            if root.right:
                fun(root.right)
        fun(root)
        return self.sum
               
        