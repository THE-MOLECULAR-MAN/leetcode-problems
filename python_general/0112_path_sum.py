#!/usr/bin/python3
# Tim H 2023
# https://leetcode.com/problems/path-sum
# Runtime: beats	94%
# Memory:  beats	5% lol
"""docstring"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    """docstring"""
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        """docstring"""
        if root is None:
            return False

        # if this is a leaf?
        # base case - nothing left to recurse
        if (root.left is None) and (root.right is None):
            if root.val == targetSum:
                return True
            else:
                return False

        # recursive case, not a leaf:
        return self.hasPathSum(root.left,  targetSum - root.val) \
            or self.hasPathSum(root.right, targetSum - root.val)
