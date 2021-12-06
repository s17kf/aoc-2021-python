#!/usr/bin/bash

if [[ $# -ne 1 ]]; then
    echo "pass day number"
    exit 1
fi

day=$1
solutionFile="solve${day}.py"

ln -s ../common .

cp ../solveTemplate.py "${solutionFile}"

sed -i "s/DAY_NUM/${day}/g" "${solutionFile}"

echo "Day ${day} initialized."
