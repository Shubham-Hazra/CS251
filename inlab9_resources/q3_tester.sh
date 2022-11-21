#!/bin/bash
var="$(python3 $1 10.129.3.3)" 
if [[ $var == "YES" ]]; then
    echo "Testcase 1 passed"
else
    echo "Testcase 1 failed for intput 10.129.3.3"
fi
var="$(python3 $1 103.27.9.152)" 
if [[ $var == "NO" ]]; then
    echo "Testcase 2 passed"
else
    echo "Testcase 2 failed for intput 103.27.9.152"
fi
var="$(python3 $1 10.130.154.1)"
if [[ $var == "YES" ]]; then
    echo "Testcase 3 passed"
else
    echo "Testcase 3 failed for intput 10.130.154.1"
fi
