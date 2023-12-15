#!/usr/bin/python3
# Tim H 2023
# https://leetcode.com/problems/create-a-dataframe-from-list/description/
# Problem: 2877
# Runtime: beats	96%
# Memory:  beats	17%
"""docstring"""

import pandas as pd


def createDataframe(student_data: list[list[int]]) -> pd.DataFrame:
    """docstring"""
    return pd.DataFrame(student_data, columns=['student_id', 'age'])
