#!/bin/bash

sed -n '/^[a-zA-Z0-9!#$%&*+-/=?^_{|]\+\(\.[a-zA-Z0-9_/]\+\)\?@[a-z]\+\.[a-z]\+\(\.[a-z]\)\?/p' $1 > valid.txt