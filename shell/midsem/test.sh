#!/bin/bash
echo enter value 1
read a
echo enter value 2
read b
echo enter operation
read o

if [[ $o == '+' ]]
then
	s=` expr $a + $b`
elif [[ $o == '-' ]]
then
	s=` expr $a - $b`
elif [[ $o == '*' ]]
then
	s=` expr $a \* $b`
elif [[ $o == '/' ]]
then
	if [[ $b -ne 0 ]]
	then
		s=$(echo "scale=3; $a/$b" | bc)
	fi
fi

echo final value: $s
