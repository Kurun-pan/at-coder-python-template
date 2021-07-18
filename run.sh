#!/bin/zsh

if [[ $# != 1 ]]; then
    echo "対象の問題番号を指定してね [a-f]"
    exit 1
else
    python3 $1.py
fi
