#!/bin/bash
n=`pwd`
cd ~; find ~ -name *.py &

echo "PID of process in background (sorting of file): $!"
echo $! | kill -s KILL
echo process killed
cd $n