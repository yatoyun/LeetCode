#
# @lc app=leetcode id=543 lang=python3
#
# [543] Diameter of Binary Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.max_diameter = 0
        
    def recursive_dfs(self, current_node: TreeNode) -> int:
        if current_node is None:
            return 0
        left = self.recursive_dfs(current_node.left)
        right = self.recursive_dfs(current_node.right)
        if left + right > self.max_diameter:
            self.max_diameter = left + right
        
        return max(left, right) + 1
    
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.recursive_dfs(root)
        return self.max_diameter
# @lc code=end

