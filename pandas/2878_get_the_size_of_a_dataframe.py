#!/usr/bin/python3
# Tim H 2023
# https://leetcode.com/problems/get-the-size-of-a-dataframe/description/
# Problem: 2878
# Runtime: beats	%
# Memory:  beats	%
"""docstring"""

import pandas as pd


def getDataframeSize(players: pd.DataFrame) -> list[int]:
    """docstring"""
    return list(players.shape)
