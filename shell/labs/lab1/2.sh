#!/bin/bash

echo enter radius of circle
read r
area=$(echo "scale=2; $r*$r*3.14"|bc)
echo $area
