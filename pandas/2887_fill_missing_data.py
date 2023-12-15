#!/usr/bin/python3
# Tim H 2023
# Runtime:  beats 51%
# Memory:   beats 50%
# https://leetcode.com/problems/fill-missing-data/description/?envType=study-plan-v2&envId=introduction-to-pandas&lang=pythondata
# https://pandas.pydata.org/docs/user_guide/missing_data.html
# https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.fillna.html

# Be mindful that in Python (and NumPy):
#   the nan's don’t compare equal,
#   but None's do.
# Note that pandas/NumPy uses the fact that np.nan != np.nan,
# and treats None like np.nan.

"""docstring"""

import pandas as pd


def fillMissingValues(products: pd.DataFrame) -> pd.DataFrame:
    """docstring"""
    # products["quantity"] = products["quantity"].fillna(0)
    products["quantity"].fillna(0, inplace=True)
    return products

# dff.where(pd.notna(dff), dff.mean(), axis="columns")
