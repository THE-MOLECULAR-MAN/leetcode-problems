#!/bin/bash
# Tim H 2023
find . -not -path '*/.*' -type f -name '*-*.py' \
    -exec bash -c 'git mv $0 ${0//-/_}' {} \;
