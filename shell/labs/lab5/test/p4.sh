echo enter a filename to inset html tags
read f1
sed  -i '1 i <HTML> ' $f1
sed -i ' $ a </HTML>' $f1

echo 'enter the filenmame to replce | by :'
read f2
sed -i '1,3s/|/:/g' $f2

