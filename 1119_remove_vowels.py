#!/usr/bin/python3
# Tim H 2023
import re


class Solution:
    def removeVowels(self, s: str) -> str:
        return re.sub(r"[a,e,i,o,u]", "", s)
