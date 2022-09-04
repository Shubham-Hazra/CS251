#!/bin/bash

awk -v file2="$2" -v num_keys="$3" 'BEGIN{k=0; 
num=0;
ORS=" "}
{
	{	
		if(NR>1 && NR<num_keys+1)
		{
			key_pair=$1
			split(key_pair,a,"-")
			keys[num]=a[1]
			values[num]=a[2]
			num++;
		}
	}
}
END{
	print "sed"
	for(i=0;i<num;i++)
	{
		
		print "-e \047s/\\b"keys[i]"\\b/___"values[i]"___/g\047"
	}
	print "-e \047s/___//g\047"
	print "-z -e \047s/\\n/ /g\047"
	print file2
}' $1|sh

