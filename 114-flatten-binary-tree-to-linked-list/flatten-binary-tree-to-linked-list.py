# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def flatten(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: None Do not return anything, modify root in-place instead.
        """
        arr=[]
        ans=[]
        def preorder(node):
            if node:
                arr.append(node)
                preorder(node.left)
                preorder(node.right)
        preorder(root)
        n=len(arr)
        for i in range(len(arr)-1):
            arr[i].left=None
            arr[i].right=arr[i+1]
        if arr:
            arr[-1].left=None
            arr[-1].right=None
        

        
                
        