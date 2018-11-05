#!/bin/bash
if [[ -f $1 ]]
	then
	od -bc $1
else
	echo "File does not exist"
	exit 1
fi