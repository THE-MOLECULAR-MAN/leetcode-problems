#!/usr/bin/python3
# Tim H 2023
# https://leetcode.com/problems/valid-sudoku/
"""docstring"""
import re


def hasDuplicates(s: str) -> bool:
    """docstring"""
    res = re.sub("[^0-9]", "", s)
    return len(set(res)) != len(res)


class Solution:
    """docstring"""

    def isValidSudoku(self, board: List[List[str]]) -> bool:
        """docstring"""
        # horizonal line test
        i = 0
        while i < 9:
            res = board[i]
            if hasDuplicates(str(res)):
                return False
            i += 1

        # vertical line test
        i = 0
        board_T = list(map(list, zip(*board)))
        while i < 9:
            res = board_T[i]
            if hasDuplicates(str(res)):
                return False
            i += 1

        # 3x3 test
        index_list = [0, 3, 6]
        for r in index_list:
            for c in index_list:
                top_row = board[r][c:c+3]
                mid_row = board[r+1][c:c+3]
                bot_row = board[r+2][c:c+3]
                res = top_row + mid_row + bot_row
                if hasDuplicates(str(res)):
                    return False
        return True
