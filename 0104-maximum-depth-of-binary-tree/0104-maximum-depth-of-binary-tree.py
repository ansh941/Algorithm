# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if root == None:
            return 0
        if root.left == None and root.right == None:
            return 1
        else:
            left, right = 0,0
            if root.left != None:
                left = self.maxDepth(root.left)
            if root.right != None:
                right = self.maxDepth(root.right)
            if left < right:
                depth = right
            else:
                depth = left
            return depth+1