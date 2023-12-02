#!/usr/local/bin/python3.12
# Running in Visual Studio venv
# Tim H 2023
# https://leetcode.com/problems/employees-earning-more-than-their-managers/description/

# References/documentation:
# https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.merge.html
# https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.map.html
# https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.set_index.html
"""docstring"""

import pandas as pd

# average version, simple:
# .merge:
#       Runtime:  583 ms, beats 33%
#       Memory:   61 MB,  beats 76%
#       adding copy=False slows it down, only saves 1 MB out of 61 MB of RAM


def find_employees(employee: pd.DataFrame) -> pd.DataFrame:
    """docstring"""
    employer_lookup = employee.merge(
        employee, how='inner', left_on="managerId", right_on="id")
    # print(employer_lookup)
    employer_lookup = employer_lookup[employer_lookup["salary_x"]
                                      > employer_lookup["salary_y"]][["name_x"]]
    return employer_lookup.rename(columns={"name_x": "Employee"})


# fastest version:
# using .map, .set_index, and []
#       Runtime:  417 ms, beats 99%
#       Memory:   60 MB,  beats 96%
def find_employees(employee: pd.DataFrame) -> pd.DataFrame:
    """docstring"""
    result_df = employee[employee['salary'] > employee['managerId'].map(
        employee.set_index('id')['salary'])]
    result_df = result_df[['name']].rename(columns={'name': 'Employee'})
    return result_df
