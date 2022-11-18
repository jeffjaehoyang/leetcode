# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        result = self.dfs(root, float('inf'), float('-inf'))
        return result

    def dfs(self, root: Optional[TreeNode], max_val: int, min_val: int) -> bool:
        if not root:
            return True
        condition_one = root.val > min_val and root.val < max_val
        condition_two = self.dfs(root.left, root.val, min_val)
        condition_three = self.dfs(root.right, max_val, root.val)
        return condition_one and condition_two and condition_three
