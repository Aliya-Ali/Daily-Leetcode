# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        res1 = []
        res2 = []
        def leave(root, res):
            if root.left == None and root.right == None:
                res.append(root.val)
                return
            
            if root.left:
                leave(root.left, res)
            if root.right:
                leave(root.right, res)
                
        leave(root1, res2)
        leave(root2, res1)
        print(res1)
        print(res2)
        if res1 == res2:
            return True
        return False
        