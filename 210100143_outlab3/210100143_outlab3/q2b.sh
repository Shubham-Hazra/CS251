#!/bin/bash

dir=$1
cd $1
ls|awk '{ old = $0
	yy = substr(old,5,2)
	dd = substr(old,8,2)
	mm = substr(old,11,2)
	img_no = substr(old,14,9)
	print "mv "old" "dd"-"mm"-20"yy"_"img_no
	}'|sh
cd ..
