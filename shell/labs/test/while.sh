#!/bin/bash
echo input integer
read n
for ((i = 0; i <= n; i++))
do	
	echo $i
	p=`(echo(expr $i + $n)|bc)`
	echo $p
done