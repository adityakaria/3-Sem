#!/bin/bash

echo enter two numbers
read a
read b
echo enter 1 to add 2 to subtract 3 to multiply 4 to divide
read o
if [ $o == 1 ]
    then
	var=` expr $a + $b `
	
elif [ $o == 2 ]
    then
	var=` expr $a - $b `

elif [ $o == 3 ]
    then
	var=` expr $a \* $b `
elif [ $o == 4 ]
    then
	var=$(echo "scale=3; $a/$b"|bc)
fi
echo $var
