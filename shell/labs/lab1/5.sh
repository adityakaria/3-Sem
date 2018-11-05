#!/bin/bash

echo enter number
read n
a=0
while [ "$a" -le "$n" ]
do
	s=` expr $s + $a `
    a=` expr $a + 1`
done
echo $s
