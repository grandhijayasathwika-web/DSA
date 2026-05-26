# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def minDepth(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        def fun(node):
            if not node:return 0
            if not node.right:
                return fun(node.left)+1
            if not node.left:
                return fun(node.right)+1
            return min(fun(node.left),fun(node.right))+1
        return fun(root)
            

        