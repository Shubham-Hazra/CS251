#!/bin/bash

sed -z -e's/\./$/g' -z -e 's/\$\n/:)\n/g' $1
 
