#!/usr/bin/python3
# Tim H 2023
# https://leetcode.com/problems/range-sum-of-bst/
# https://leetcode.com/problems/range-sum-of-bst/solutions/4435252/python3-recursive-solution-with-3-simple-functions-beats-99-runtime-99-memory/
# Runtime: beats:  99.99%
# Memory:  beats:  99.85%
# SHOULD_PUBLISH_SOLUTION
"""Solution for problem 938 - Range Sum of BST by THE-MOLECULAR-MAN"""

from typing import Optional

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    """class defined by leetcode problem set"""

    def return_value_in_range(self, node, low, high):
        """returns the node's value if it is between low and high
        returns 0 if the node is null"""
        # this one has to go first since node.val will throw error
        # could use a try/except/finally instead.
        # https://www.geeksforgeeks.org/try-except-else-and-finally-in-python/
        if node is None:
            return 0
        if low <= node.val <= high:
            return node.val
        return 0

    def is_leaf(self, node):
        """returns True if the current node is a leaf (has no children nodes)"""
        if node is None:
            return True
        return (node.left is None) and (node.right is None)

    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        """recursive function to sum a node tree's values if they're between
        low and high"""

        # base case:
        if self.is_leaf(root):
            return self.return_value_in_range(root, low, high)

        # recursive case, not a leaf
        # add the current node's value to its children
        return self.return_value_in_range(root, low, high) + \
            self.rangeSumBST(root.left,    low, high) + \
            self.rangeSumBST(root.right,   low, high)
