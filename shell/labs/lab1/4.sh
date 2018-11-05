#!/bin/bash
echo enter no. of elements
read n
a=0
s=0
while [ "$a" -lt "$n" ]
do
	read num
	s=$(echo "scale=3; $s+$num"|bc)
	a=` expr $a + 1 `
done
avg=$(echo "scale=3; $s / $n"|bc)
echo $avg