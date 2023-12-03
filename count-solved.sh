#!/bin/bash
# Tim H 2023

# count the number of solved for comparing to LeetCode profile page

find . -mindepth 2 -type f -not -path '*/.*'  -not -ipath '*unfinished*' \
    -iname '*.py' -o -iname '*.sql' -o -iname '*.sh' | wc -l
   