#!/bin/bash
echo "Enter the name of file or directory: "
read a
if [[ -d $a ]]
then
	echo "'$a' is a directory"
	echo "Contents of the directory are: "
	ls $a
elif [[ -f $a ]]
then
	echo "'$a' is a file"
	echo "Contents of the file are: "
	cat $a
else
	echo "'$a' does not exist"
	exit 1
fi
