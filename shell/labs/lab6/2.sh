#!/bin/bash
sort small.dict | uniq > sorted_small.dict &

echo "PID of process in background (sorting of file): $!"

n=`ps | wc -l`
n="$n - 1" | bc
echo "Number of processes running in the background: $n"