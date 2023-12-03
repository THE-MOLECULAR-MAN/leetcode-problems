#!/bin/bash
# Tim H 2023


find . -type f -not -path '*/.*'  -not -ipath '*unfinished*' \
    -iname '*.py' -exec autopep8 --in-place {} \+

find . -type f -not -path '*/.*'  -not -ipath '*unfinished*' \
    -iname '*.py' -exec pylint  {} \+

