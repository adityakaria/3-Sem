#!/bin/bash
echo "Enter your option: "
echo "(1) Decimal number to binary"
echo "(2) Binary to decimal"
echo "(3) Binary to hexadecimal"
echo "(4) Hexadecimal to Decimal"
read choice

case $choice in
1)
	read -p "Enter decimal number " ip
	echo "obase=2; $ip" | bc
	;;
2)
	read -p "Enter binary number " ip
	echo "ibase=2; $ip" | bc
	;;
3)
	read -p "Enter Binary number " ip
	echo "obase=16; ibase=2; $ip" | bc
	;;
4)
	read -p "Enter Hexadecimal number " ip
	echo "ibase=16; $ip" | bc
	;;
esac

echo done
