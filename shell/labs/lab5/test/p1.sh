t=` echo $(date +"%H")`
if [ $t -ge 0 -a $t -lt 12 ]
then
echo good morning
fi
if [ $t -ge 12 -a $t -lt 18 ]
then 
echo good afternoon 
fi
if [ $t -ge 18 -a $t -lt 20 ]
then
echo good evening
fi
if [ $t -ge 20 ]
then
echo good night
fi

