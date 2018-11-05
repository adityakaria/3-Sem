#!/bin/bash

array=[]

for i in {0..4}
do
	echo "Enter the Element $i"
	read array[$i]
done

for i in {0..4}
do
	for j in {0..3}
	do
		if [ ${array[$j]} -gt ${array[$j+1]} ]
			then
			temp=${array[$j]}
			array[$j]=${array[$j+1]}
			array[$j+1]=$temp
		fi
	done
done




max=${array[4]}
min=${array[0]}
count=1

prev=${array[0]}


	
for j in {0..3}
do
	curr=${array[$j]}
	if [ ${array[$j+1]} -eq $curr ]
		then
		((count++))
	else
		echo "$curr appears $count times"
		count=1
	fi
done

if [ $count -eq 1 ]
	then
	echo "${array[4]} appears 1 times"
fi


echo "MAX = $max"
echo "MIN = $min"