# https://leetcode.com/problems/duplicate-emails/description
# 
import pandas as pd

def duplicate_emails(person: pd.DataFrame) -> pd.DataFrame:
    y = person[person.duplicated(['email'])]
    z = pd.DataFrame()
    z['Email'] = pd.unique(y['email'])
    return z
