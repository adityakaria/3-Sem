#!/bin/sh

x=0

if [ $1 -lt $x ] || [ $2 -lt $x ]
then
echo "Invalid Input,Please Try Again"
elif [ $1 -gt $2 ]
then
echo "scale=2; $2/$1" | bc
else
echo "scale=2; $1/$2" | bc
fi
