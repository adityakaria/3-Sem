#!/bin/bash
rm k.txt
for t in *
do
	if [ -f $t ]
	then
		echo $t >> k.txt
	fi
done
grep -E "^[AEIOUaeiou]" k.txt
