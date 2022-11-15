# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        diameter, _ = self.dfsHelper(root)
        return diameter

    def dfsHelper(self, root: Optional[TreeNode]):
        if not root:
            return (0, 0)
        leftRootMax, leftArmMax = self.dfsHelper(root.left)
        rightRootMax, rightArmMax = self.dfsHelper(root.right)
        maxAsArm = 1 + max(leftArmMax, rightArmMax)
        maxAsRoot = max(leftRootMax, rightRootMax, leftArmMax + rightArmMax)
        return (maxAsRoot, maxAsArm)
