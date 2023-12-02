#!/usr/bin/python3
# Tim H 2023
# https://leetcode.com/studyplan/introduction-to-pandas/
# https://leetcode.com/problems/drop-duplicate-rows/?envType=study-plan-v2&envId=introduction-to-pandas&lang=pythondata
# Runtime:  beats 94%
# Memory:   beats 92%
"""docstring"""

import pandas as pd


def dropDuplicateEmails(customers: pd.DataFrame) -> pd.DataFrame:
    """docstring"""
    return customers.drop_duplicates(subset=['email'])
    # , keep='first')
    # , inplace=True)
