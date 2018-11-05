#!/bin/bash
read -p "Enter UNIX marks: " unix
read -p "Ente JAVA marks: " java
read -p "Enter DSA marks: " dsa

total=`expr $unix + $java + $dsa`
total=`expr $total / 3`

echo "average marks: $total"

if [[ $total -ge 70 ]]
then
	echo "Distinction"
elif [[ $total -ge 60 ]]; then
	#statements
	echo "First Class"
elif [[ $total -ge 50 ]]; then
	#statements
	echo "Second Class"
elif [[ $total -ge 40 ]]; then
	#statements
	echo "Third Class"
else
	echo "Fail"
fi
