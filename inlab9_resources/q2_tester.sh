#!/bin/bash
rm -f zipcodesDB.db
var="$(python3 $1 AL)" 
if [[ $var == "19003,35739,38449,73401,73402,73403" ]]; then
    echo "Testcase 1 passed"
else
    echo "Testcase 1 failed for intput AL"
fi
rm -f zipcodesDB.db
var="$(python3 $1 CA)" 
if [[ $var == "96044" ]]; then
    echo "Testcase 2 passed"
else
    echo "Testcase 2 failed for intput CA"
fi
rm -f zipcodesDB.db
var="$(python3 $1 "AU")"
if [[ $var == "NOT FOUND" ]]; then
    echo "Testcase 3 passed"
else
    echo "Testcase 3 failed for intput AU"
fi