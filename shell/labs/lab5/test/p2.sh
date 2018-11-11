#!/bin/bash

i="y"
while [ $i = "y" ]
do

echo "1. View Database "
echo "2. Add Record "
echo "3. Delete Record "
echo "9. Exit "
echo "Enter choice: "
read ch
case $ch in
    1) cat 1.txt 
    	echo;;
    2) echo "Enter new std roll no. "
		read rn
		echo "Enter new name:"
		read nm
		echo "Enter semester "
		read sem
		echo "enter sub1 marks"
		read s1
		echo enter sub2 mrks
		read s2
		echo enter sub3 marks
		read s3
		echo "$rn    $nm    $sem   $s1  $s2   $s3 ">> 1.txt;;
    3) echo "Enter rn"
		read rn
		grep -v "$rn" 1.txt > dbs 
		cp dbs 1.txt  
		echo "Record is deleted"
		cat 1.txt;;           
    5) exit;;
    *) ;;
esac
done