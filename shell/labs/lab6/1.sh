#!/bin/bash

n=whoami
echo "Processes by user: $n"
ps -u `whoami`


echo "PID of the current shell: "
ps $$

