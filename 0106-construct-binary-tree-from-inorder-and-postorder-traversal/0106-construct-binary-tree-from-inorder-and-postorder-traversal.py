# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# postorder = 전 후 중
# inorder = 전 중 후
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        if len(inorder) == 0 or len(postorder) == 0:
            return None
        
        root = TreeNode(postorder[-1])
        root_idx = inorder.index(root.val)
        
        left_subsize = root_idx
        right_subsize = len(inorder)-root_idx-1
        
        root.left = self.buildTree(inorder[:root_idx], postorder[:left_subsize])
        root.right = self.buildTree(inorder[1+root_idx:], postorder[left_subsize:left_subsize+right_subsize])
        
        return root