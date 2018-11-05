#!/bin/bash
echo "Choose:"
echo "1: Strings are non empty"
echo "2: Strings are same"
echo "3: Strings are palindrome"
read option
str=''
case $option in
1)
	echo "Enter String: "
	read s
	if [ -z $s ]
	then
		echo String is empty
	else
		echo String is non-empty
	fi
	;;
2)
	echo "Enter String 1: "
	read s1
	echo "Enter String 2: "
	read s2
	if [ $s1 == $s2 ]
	then
		echo Strings are same
	else
		echo Strings are different
	fi
	;;
3)
	read -p "Enter string: " string
	if [[ $(rev <<< "$string") == "$string" ]]; then
    	echo String is Palindrome
	else
		echo String is not a palindrome
	fi
	;;
esac