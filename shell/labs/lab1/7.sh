#!/bin/bash

area=$(echo "scale=3; $1 * $2"|bc)
echo "area = $area"
