#!/usr/bin/python3
# Tim H 2023
# https://leetcode.com/problems/change-data-type/?envType=study-plan-v2&envId=introduction-to-pandas&lang=pythondata
# https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.astype.html
# Runtime:  beats 99.7%
# Memory:   beats 57.8%
"""docstring"""

import pandas as pd

def changeDatatype(students: pd.DataFrame) -> pd.DataFrame:
    # copy=False
    students.grade = students.grade.astype('int64')
    return students

# new = s.apply(lambda num : num + 5)
# https://www.geeksforgeeks.org/python-pandas-apply/
