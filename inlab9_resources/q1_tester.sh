#!/bin/bash
var="$(python3 $1 "CS228")" 
if [[ $var == "KAIST:CS402;NUS:CS3234" ]]; then
    echo "Testcase 1 passed"
else
    echo "Testcase 1 failed for intput CS228"
fi
var="$(python3 $1 "CS302")" 
if [[ $var == "NUS:CS4215;SFU:CMPT379" ]]; then
    echo "Testcase 2 passed"
else
    echo "Testcase 2 failed for intput CS302"
fi
var="$(python3 $1 "CS416")"
if [[ $var == "NTU:CE4024" ]]; then
    echo "Testcase 3 passed"
else
    echo "Testcase 3 failed for intput CS416"
fi
var="$(python3 $1 "CS419M")" 
if [[ $var == "NOT FOUND" ]]; then
    echo "Testcase 4 passed"
else
    echo "Testcase 4 failed for intput CS419M"
fi
var="$(python3 $1 "CS251")" 
if [[ $var == "NOT FOUND" ]]; then
    echo "Testcase 5 passed"
else
    echo "Testcase 5 failed for intput CS251"
fi
var="$(python3 $1 "CS337")" 
if [[ $var == "NUS:CS3243 (AI), CS3244 (ML);SFU:CMPT310+CMPT726" ]]; then
    echo "Testcase 6 passed"
else
    echo "Testcase 6 failed for intput CS337"
fi