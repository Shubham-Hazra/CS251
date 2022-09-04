#!/bin/bash

ls $1|awk '{
length=0
for(i=1;i<=NF;i++){
	found=1
	for(j=0;j<length;j++){
	if(arr[j]==$i){found=0; break}
	else {continue}
	}
	if(found==0){continue}
	else {
		arr[length] = $i 
		length++
}
}
print length
}' $1
