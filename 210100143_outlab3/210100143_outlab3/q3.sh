#!/bin/bash


if [ "$#" == "1" ]; then
{
		awk 'BEGIN{
		num_chars=0;
		num_words=0;
		num_lines=0;
		num_paras=0;
		blanks=1;
		consecutive=0;
		}
		{
			if(NR==1 && NF==0)
			{
				blanks--;
			}
		
			for (i=1;i<=NF;i++)
			{
				if($i!=" ")
				{
					num_words++;
					num_chars=num_chars+length($i)
				}
			}
			if(NF==0)
			{	
				if(consecutive==0)
				{
					blanks++;
					consecutive++;
				}
			}
			else
			{
				consecutive=0;
			}
			num_lines=NR
		}
	END{ if(NF==0)
	{blanks--} 
	num_paras=blanks
	print num_chars" characters, "num_words" words, "num_lines" lines, "num_paras" paragraphs"}' $1
}
elif [ "$#" == "2" ]
then
	{
		if [ $2 == "-lines" ]
	then
	{
	awk 'BEGIN{
		num_chars=0;
		num_words=0;
		num_lines=0;
		num_paras=0;
		blanks=1;
		consecutive=0;
		}
		{
			if(NR==1 && NF==0)
			{
				blanks--;
			}
		
			for (i=1;i<=NF;i++)
			{
				if($i!=" ")
				{
					num_words++;
					num_chars=num_chars+length($i)
				}
			}
			if(NF==0)
			{	
				if(consecutive==0)
				{
					blanks++;
					consecutive++;
				}
			}
			else
			{
				consecutive=0;
			}
			num_lines=NR
		}
	END{ if(NF==0)
	{blanks--} 
	num_paras=blanks
	print num_lines" lines"}' $1
}
	elif [ $2 == "-words" ]
	then
	{
		awk 'BEGIN{
		num_chars=0;
		num_words=0;
		num_lines=0;
		num_paras=0;
		blanks=1;
		consecutive=0;
		}
		{
			if(NR==1 && NF==0)
			{
				blanks--;
			}
		
			for (i=1;i<=NF;i++)
			{
				if($i!=" ")
				{
					num_words++;
					num_chars=num_chars+length($i)
				}
			}
			if(NF==0)
			{	
				if(consecutive==0)
				{
					blanks++;
					consecutive++;
				}
			}
			else
			{
				consecutive=0;
			}
			num_lines=NR
		}
	END{ if(NF==0)
	{blanks--} 
	num_paras=blanks
	print num_words" words"}' $1
}
elif [ $2 == "-chars" ]
	then
	{
		awk 'BEGIN{
		num_chars=0;
		num_words=0;
		num_lines=0;
		num_paras=0;
		blanks=1;
		consecutive=0;
		}
		{
			if(NR==1 && NF==0)
			{
				blanks--;
			}
		
			for (i=1;i<=NF;i++)
			{
				if($i!=" ")
				{
					num_words++;
					num_chars=num_chars+length($i)
				}
			}
			if(NF==0)
			{	
				if(consecutive==0)
				{
					blanks++;
					consecutive++;
				}
			}
			else
			{
				consecutive=0;
			}
			num_lines=NR
		}
	END{ if(NF==0)
	{blanks--} 
	num_paras=blanks
	print num_chars" characters"}' $1
}
	
	elif [ $2 == "-paras" ]
	then
	{
		awk 'BEGIN{
		num_chars=0;
		num_words=0;
		num_lines=0;
		num_paras=0;
		blanks=1;
		consecutive=0;
		}
		{
			if(NR==1 && NF==0)
			{
				blanks--;
			}
		
			for (i=1;i<=NF;i++)
			{
				if($i!=" ")
				{
					num_words++;
					num_chars=num_chars+length($i)
				}
			}
			if(NF==0)
			{	
				if(consecutive==0)
				{
					blanks++;
					consecutive++;
				}
			}
			else
			{
				consecutive=0;
			}
			num_lines=NR
		}
	END{ if(NF==0)
	{blanks--} 
	num_paras=blanks
	print num_paras" paragraphs"}' $1
}
	
	fi
}
fi



