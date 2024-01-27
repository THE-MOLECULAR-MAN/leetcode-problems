#!/usr/bin/python3
# Tim H 2023
# https://leetcode.com/problems/same-tree/
"""docstring"""
# Runtime: beats	97%
# Memory:  beats	9%


from typing import Optional

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    """docstring"""

    def is_null_leaf(self, node):
        """returns True if the current node is a leaf (has no children nodes)"""
        if node is None or node is []:
            return (node.val is None)
        return (node.left is None) and (node.right is None)

    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        """docstring"""
        # exit early:
        # the order of these if statements matters a lot:
        if self.is_leaf(p) and self.is_leaf(q):
        p is None and q is None or \
                p == [] and q == []:
            return True

        if (p is None and q is not None) or \
                (p is not None and q is None):
            return False

        if p.val is None and q.val is None:
            return True

        if p.val != q.val:
            return False

        # if this is a leaf?
        # base case
        if (p.left is None) and (p.right is None) and \
            (q.left is None) and (q.right is None) and \
                q.val == p.val:
            return True
        # else:
        #    return False

        # recursive case, not a leaf - use AND
        return self.isSameTree(p.left,  q.left) and \
            self.isSameTree(p.right, q.right)
