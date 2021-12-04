#!/usr/bin/bash

if [[ $# -ne 1 ]]; then
    echo "pass day number"
    exit 1
fi

day=$1

ln -s ../common/common.py

cp ../solveTemplate.py solve${day}.py

echo "Day ${day} initialized."
