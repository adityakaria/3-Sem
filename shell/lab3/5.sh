#!/bin/bash
echo "Processor information"
#cat /proc/cpuinfo
sysctl -n machdep.cpu.brand_string

echo "Kernel information: "
#more /proc/version
uname -r #-a
