# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def evaluateTree(self, root: Optional[TreeNode]) -> bool:
        def inverter(root):
            if root.left == None and root.right == None:
                return root.val
            
            left = inverter(root.left)
            right = inverter(root.right)
            
            if root.val == 3:
                return (left and right)
            elif root.val == 2:
                return (left or right)
            
            
        return inverter(root)
        