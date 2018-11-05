#!/bin/bash

echo current home directory:
echo $HOME
echo
echo Current username:
whoami
echo
echo Today is:
echo `date +%d-%m-%y`
echo
echo "No of users logged in :"
who | wc -l
echo
echo terminal number:
tty

