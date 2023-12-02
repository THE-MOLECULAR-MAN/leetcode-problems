#!/usr/bin/python3
# Tim H 2023
# https://leetcode.com/problems/display-the-first-three-rows/description/
# Runtime:  beats 22%
# Memory:   beats 82%
"""docstring"""

import pandas as pd


def selectFirstRows(employees: pd.DataFrame) -> pd.DataFrame:
    """docstring"""
    return employees.head(3)
