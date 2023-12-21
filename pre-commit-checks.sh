#!/bin/bash
# Tim H 2023

clear

# rename files that have a hyphen to use underscore
find . -not -path '*/.*' -type f -name '*-*.py' \
    -exec bash -c 'git mv $0 ${0//-/_}' {} \;

# auto-fix pep8 issues in .py files
# ignore any files that aren't finished
find . -type f -not -path '*/.*'  -not -iname '*UNFINISHED*' \
    -iname '*.py' -exec autopep8 --in-place {} \+

# display any remaining Python lint/syntax issues in the files
find . -type f -not -path '*/.*'  -not -iname '*UNFINISHED*' \
    -iname '*.py' -exec pylint  {} \+

# display any Bash lint issues:
find . -type f -not -path '*/.*'  -not -iname '*UNFINISHED*' \
    -iname '*.sh' -exec shellcheck  {} \+

# display any SQL lint issues:
find . -type f -not -path '*/.*'  -not -iname '*UNFINISHED*' \
    -iname '*.sql' -exec sql-lint  {} \+

# display diffs for any changed files, no pagination
git diff --name-only HEAD^ | git --no-pager diff
