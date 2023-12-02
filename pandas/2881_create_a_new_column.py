#!/usr/bin/python3
# Tim H 2023
# https://leetcode.com/problems/create-a-new-column/?envType=study-plan-v2&envId=introduction-to-pandas&lang=pythondata
# https://leetcode.com/studyplan/introduction-to-pandas/
# Runtime:  beats 98%
# Memory:   beats 78%
"""docstring"""


import pandas as pd


def createBonusColumn(employees: pd.DataFrame) -> pd.DataFrame:
    """docstring"""
    employees['bonus'] = employees['salary'] * 2
    return employees
