#!/bin/bash
p=0
echo "sum of cubes of digits equal to the number are:"
for i in {1..999}
do
	p=$i
	sum=0
	while [ $p -gt 0 ]
	do
		x=$(($p % 10))
		x=$(($x*$x*$x))
		sum=$(($sum+$x))
		p=$(($p/10))
	done

	if [ $sum -eq $i ]
	then

		echo "$i"
	fi
done
