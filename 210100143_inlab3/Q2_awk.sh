#!/bin/bash

awk '
{
 	num_digits=NF;
	for(i=1;i<=NF;i++)
	{
		if($i=="a")
		{digits[i-1]=10}
		else if($i=="b")
                {digits[i-1]=11}
		else if($i=="c")
                {digits[i-1]=12}
		else {digits[i-1]=$i}
	}
	#for(i=0;i<NF;i++){print digits[i]}
        base=8+2*(NR%3)
	sum=0;
        for(i=0;i<num_digits;i++)
        {
		mult=1;
        	for(j=0; j<num_digits-i-1; j++){
                mult=mult*base;
        	}
                sum=sum+digits[i]*mult;
        }
print sum
}' $1
