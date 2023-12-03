#!/usr/bin/python3
# Tim H 2023
# https://leetcode.com/studyplan/introduction-to-pandas/
# https://leetcode.com/problems/drop-missing-data/description/?envType=study-plan-v2&envId=introduction-to-pandas&lang=pythondata

# https://saturncloud.io/blog/how-to-delete-rows-with-null-values-in-a-specific-column-in-pandas-dataframe/#:~:text=Deleting%20rows%20with%20null%20values%20in%20a%20specific%20column%20can,values%20in%20the%20specified%20column.
# Runtime:  beats 98%
# Memory:   beats 
"""docstring"""

import pandas as pd

def dropMissingData(students: pd.DataFrame) -> pd.DataFrame:
    # the runtime is highly variable, running the same thing twice in a row
    # got me "beats 95%" once and then "beats 18%" the next time
    students.dropna(subset=['name'], inplace=False)
    return students

    # beats only 9% in runtime, 18% in memory:
    students.dropna(subset=['name'], inplace=True)
    return students
