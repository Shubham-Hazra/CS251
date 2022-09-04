#!/bin/bash
num=$1
a=0
b=1
for((i=0;i<$1;i++))
do
	echo -n ${a}
	echo -n " "
	temp=$((b))
	b=$((a+b))
	a=$((temp))
done
echo ""
