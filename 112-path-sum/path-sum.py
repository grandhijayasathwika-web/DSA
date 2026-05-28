# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def hasPathSum(self, root, targetSum):
        """
        :type root: Optional[TreeNode]
        :type targetSum: int
        :rtype: bool
        """
        
        
        def fun(node,summ):
            if not node:return False
            if not node.left and not node.right:
                summ+=node.val
                if summ==targetSum:
                    return True

            return fun(node.right,summ+node.val) or fun(node.left,summ+node.val)
        return fun(root,0)==True