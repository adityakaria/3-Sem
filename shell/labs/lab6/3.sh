#!/bin/bash
n=`pwd`
pip install root &
echo $!
kill $!
echo "PID of process in background (sorting of file): $!"
echo process killed