#!/bin/bash


# echo "Addition of matrices."

# arr1=()
# arr2=()
# arr3=()

# sum=0
# len=${#arr1[@]}
# for ((i=0; i<$len; i++))
# do
#  sum=$(( ${arr1[$i]}+${arr2[$i]} )) 
#  #echo $sum
#  arr3=("${arr3[@]}" "$sum")
# done 
# echo ${arr3[@]}


echo 'enter the size of matrix rows..'
read r
echo 'enter the size of matrix columns..'
read c

a=[]
b=[]
p=[]

echo enter the elements of matrix A...
for ((i=0; $i<$r; i++))
do
	for ((j=0; $j<$c; j++))
    do
    	read a[$(($j+$i*$c))]
    done
    echo
done

echo enter the elements of matrix b...
for ((i=0; $i<$r; i++))
do
	for ((j=0; $j<$c; j++))
    do
    	read b[$(($j+$i*$c))]
    done
    echo
done


m=`expr $c * $r`


echo The sum of array is...

for ((i=0; $i<$r; i++))
do
	for ((j=0; $j<$c; j++))
    do
    	p[$(($j+$i*$c))]=$((${a[$(($j+$i*$c))]}+${b[$(($j+$i*$c))]}))
    	echo -ne "${p[$(($j+$i*$c))]}  "
    done
    echo
done
