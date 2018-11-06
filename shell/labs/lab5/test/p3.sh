#!/bin/bash

echo "Finding the empty lines"
grep -cv '\S' c.txt
echo

echo "finding files with vowels"
rm -f vow_files.txt
touch vow_files.txt
for t in *
do
	if [ -f $t ]
	then
		echo $t >> vow_files.txt
	fi
done
grep -E "^[AEIOUaeiou]" vow_files.txt
echo