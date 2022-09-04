#!/bin/bash

awk '{
	if(NR==1)
	{
		testcases=$1
	}
	
		if(NR%3==2)
		{	
			input_base=$1;
			output_base=$2;
		}
		if(NR%3==0)
		{
			num_digits1=NF;
			for(i=1;i<=NF;i++)
			{
				if($i>=0 && $i<=9)
				{digits1[i-1]=$i}
				else if($i=="a")
				{digits1[i-1]=10}
				else if($i=="b")
				{digits1[i-1]=11}
				else if($i=="c")
				{digits1[i-1]=12}
				else if($i=="d")
				{digits1[i-1]=13}
				else if($i=="e")
				{digits1[i-1]=14}
				else if($i=="f")
				{digits1[i-1]=15}
				else
				{digits1[i-1]=$i}
				
			}
			num1=0;
			for(i=0;i<num_digits1;i++)
			{
				mult=1;
				for(j=0; j<num_digits1-i-1; j++){
				mult=mult*input_base;
				}
				num1=num1+digits1[i]*mult;
			}
		}
		if(NR%3==1 && NR!=1)
		{
			num_digits2=NF;
			for(i=1;i<=NF;i++)
			{
				if($i>=0 && $i<=9)
				{digits2[i-1]=$i}
				else if($i=="a")
				{digits2[i-1]=10}
				else if($i=="b")
				{digits2[i-1]=11}
				else if($i=="c")
				{digits2[i-1]=12}
				else if($i=="d")
				{digits2[i-1]=13}
				else if($i=="e")
				{digits2[i-1]=14}
				else if($i=="f")
				{digits2[i-1]=15}
				else
				{digits2[i-1]=$i}
			}
			num2=0;
			for(i=0;i<num_digits2;i++)
			{
				mult=1;
				for(j=0; j<num_digits2-i-1; j++){
				mult=mult*input_base;
				}
				num2=num2+digits2[i]*mult;
			}
			sum = num1+num2;
			num_digits=0
			i=0
			while(sum>0)
			{	
				digits[i]=int(sum%output_base)
				sum=int(sum/output_base)
				num_digits++
				i++
			}
			for(i=num_digits-1;i>=0;i--)
			{
				printf "%d ",digits[i]
				
			}
			printf "\n" 
		}
		
		
}' $1 > $2
