#!/bin/bash
echo Enter Principle
read p
echo Enter time \(in years\)
read t
echo Enter rate
read rate

si=` expr $p \* $t \* $rate `
si=`expr $si / 100 `

echo $si
