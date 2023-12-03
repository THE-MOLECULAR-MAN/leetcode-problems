#!/usr/bin/python3
# Tim H 2023
# https://leetcode.com/studyplan/introduction-to-pandas/
# https://leetcode.com/problems/rename-columns/description/?envType=study-plan-v2&envId=introduction-to-pandas&lang=pythondata

# Runtime:  beats 74%
# Memory:   beats 88%
"""docstring"""

import pandas as pd

def renameColumns(students: pd.DataFrame) -> pd.DataFrame:
    """docstring"""
    new_column_names_mapping = {
        'id':    'student_id',
        'first': 'first_name',
        'last':  'last_name',
        'age':   'age_in_years'}
    
    # cannot specify axis=0 with columns=...
    # adding inplace speeds it up and reduces ram significantly
    students.rename(columns=new_column_names_mapping, inplace=True)
    return students
