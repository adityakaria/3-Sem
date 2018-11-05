#!/bin/bash
echo "Enter filename 1: "
read a
echo "Enter filename 2: "
read b

if [[ -f $a ]];
then
	echo ""
else
	echo "FILE 1 does not exist"
	exit 1
fi

if [[ -f $b ]];
then
	echo ""
else
	#statements
	echo "FILE 2 does not exist"
	exit 1
fi


echo "Copying contents from file 1 to file 2"
cat $a $b
cat $a >> $b
echo "Done"
