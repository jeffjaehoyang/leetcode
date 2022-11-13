# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

"""
A height-balanced binary tree is defined as a binary tree
in which the height of the left and the right subtree of
any node differ by not more than 1.
"""


class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        result, _ = self.dfs(root)
        return result

    def dfs(self, node: Optional[TreeNode]) -> (bool, int):
        if not node:
            return (True, 0)
        left_balanced, left_height = self.dfs(node.left)
        right_balanced, right_height = self.dfs(node.right)
        both_balanced = left_balanced and right_balanced and abs(
            left_height - right_height) <= 1
        return (both_balanced, 1 + max(left_height, right_height))
