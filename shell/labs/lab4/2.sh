sort sfile1 > file1
sort sfile2 > file2

echo comparing the two files: file1 and file2....

echo 'Checking if files are identical:'
comm file1 file2 -3 > difference.txt

if [ -s difference.txt ]
	then
	echo files are different.
else
	echo files are identical
	exit
fi

echo common elements of the two files:
comm file1 file2 -12

echo elements unique to file1:
comm file1 file2 -23

echo elements unique to file2:
comm file1 file2 -13

echo 'to make the two files identical:'
comm file1 file2 -13 >> pfile1
comm file1 file2 -23 >> pfile2

echo 'done!'

sort pfile1 > file1
sort pfile2 > file2

echo 'Now Checking if files are identical:'
comm file1 file2 -3 > difference.txt

if [ -s edifference.txt ]
	then
	echo files are different
else
	echo files are identical
	exit
fi
