#!/usr/local/bin/python3.12
# Running in Visual Studio venv
# Tim H 2023
# https://leetcode.com/problems/combine-two-tables/description/?lang=pythondata
# Runtime:  beats 95%
# Memory:   beats 84%
""" module docstring """

import pandas as pd


def combine_two_tables(person: pd.DataFrame, address: pd.DataFrame) -> pd.DataFrame:
    combined = pd.merge(person, address, how='left', on='personId')
    return combined[['firstName', 'lastName', 'city', 'state']]
