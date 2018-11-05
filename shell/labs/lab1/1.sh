#!/bin/bash
 echo enter principal
 read p
 echo enter rate
 read r
 echo enter years
 read t
 interest=$(echo "scale=3; $p * $r * $t / 100" | bc)
 echo $interest

