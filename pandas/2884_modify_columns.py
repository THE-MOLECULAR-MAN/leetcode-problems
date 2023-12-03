#!/usr/bin/python3
# Tim H 2023
# https://leetcode.com/problems/modify-columns/?envType=study-plan-v2&envId=introduction-to-pandas&lang=pythondata
# Runtime:  beats 96%
# Memory:   beats 10%
"""docstring"""

import pandas as pd

# def modifySalaryColumn(employees: pd.DataFrame) -> pd.DataFrame:
#     """docstring"""
#     employees['salary'] = employees['salary'] * 2
#     return employees

# mildly faster:


def modifySalaryColumn(employees: pd.DataFrame) -> pd.DataFrame:
    """docstring"""
    employees['salary'] *= 2
    return employees
