#!/usr/bin/python3
# Tim H 2023
# UNFINISHED
# this is really a test if it is a MIRROR image across the center
# I interpreted the problem wrong, need a whole new approach
# https://leetcode.com/problems/symmetric-tree/
"""docstring"""


from typing import Optional

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    """docstring"""
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        """docstring"""
        
        # exit early:
        # the order of these if statements matters a lot:
        if root.left is None and root.right is None or \
                root.left == [] and root.right == []:
            return True

        if (root.left is None and root.right is not None) or \
                (root.left is not None and root.right is None):
            return False

        if root.left.val is None and root.right.val is None:
            return True

        if root.left.val != root.right.val:
            return False

        # if this is a leaf?
        # base case
        if root.left.val == root.right.val:
            return True
        
        # recursive case, not a leaf - use AND
        return self.isSymmetric(root.right) and self.isSymmetric(root.left)
            # and \
            # self.isSameTree(p.right, q.right)
