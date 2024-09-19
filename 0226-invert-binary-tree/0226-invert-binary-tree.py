# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def inverter(root):
            if root.left == None and root.right == None:
                return
            if root.left:
                inverter(root.left)
            if root.right:
                inverter(root.right)
            root.left, root.right = root.right, root.left
        if root == None:
            return None
        inverter(root)
        return root
        
    def invertTree1(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return 
        
        root.left , root.right = root.right , root.left
        self.invertTree(root.left)
        self.invertTree(root.right)
        return root
        