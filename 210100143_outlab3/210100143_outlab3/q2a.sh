#!/bin/bash

awk -F, '{
	if(NR==1)
	{
		$NF = "Date"
		$(NF+1)="Time"
	}
	else
	{
		timestamp=$3
		year=substr(timestamp,1,4)
		mm=substr(timestamp,6,2)
		dd=substr(timestamp,9,2)
		hh=substr(timestamp,12,2)
		minutes=substr(timestamp,15,2)
		months[0]="January"
		months[1]="February"
		months[2]="March"
		months[3]="April"
		months[4]="May"
		months[5]="June"
		months[6]="July"
		months[7]="August"
		months[8]="September"
		months[9]="October"
		months[10]="November"
		months[11]="December"
		month_name = months[int(mm)-1]
		if(int(dd)<10)
		{
			$NF = "0"int(dd)" "month_name" "year
		}
		else
		{
			$NF = int(dd)" "month_name" "year
		}
		
		if(int(hh)==0)
		{
			$(NF+1)=12":"minutes"AM"
		}
		else if(int(hh)==12)
		{
			$(NF+1)=12":"minutes"PM"
		}
		else if(int(hh)>=13)
		{
			timehr = int(hh)-12
			if(int(hh)<22)
			{
				$(NF+1)="0"timehr":"minutes"PM"
			}
			else
			{
				$(NF+1)=timehr":"minutes"PM"
			}
			
			
			
		}
		else
		{
			if(int(hh)<10)
			{
				$(NF+1)="0"int(hh)":"minutes"AM"
			}
			else
			{
				$(NF+1)=int(hh)":"minutes"AM"
			}
			
		}
	}
	
	

}1' OFS=, $1 > $2
