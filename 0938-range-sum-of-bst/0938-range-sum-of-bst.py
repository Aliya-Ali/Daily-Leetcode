# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        self.sum = 0
        def sumBST(root):
            if root == None:
                return
            if root.val >= low and root.val <= high:
                self.sum += root.val
                sumBST(root.left)
                sumBST(root.right)
            # elif root.val == low:
            #     self.sum += root.val
            #     sumBST(root.right)
            # elif root.val == high:
            #     self.sum += root.val
            #   sumBST(root.left)
            elif root.val < low:
                sumBST(root.right)
            elif root.val > high:
                sumBST(root.left)
        sumBST(root)
        return self.sum
            
        