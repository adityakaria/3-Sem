i="y"
echo "Enter name of database "
read db
while [ $i = "y" ]
do
clear
echo "1.View the Data Base "
echo "2.View Specific Records "
echo "3.Add Records "
echo "4.Delete Records "
echo "5.Exit "
echo "Enter your choice "
read ch
    case $ch in
        1)cat $db;;
        2)echo "Enter roll number "
          read id
            grep -i "$id" $db;;
        3)echo "Enter new std roll no. "
          read rn
          echo "Enter new name:"
          read nm
          echo "Enter semester "
          read sem
          echo "enter sub1 marks"
          read s1
          echo enter sub2 mrks
          read s2
          echo enter sub3 marks
          read s3
          echo "$rn    $nm    $sem   $s1 $s2 $s3 ">>$db;;
        4)echo "Enter rn"
          read rn
      
        grep -v "$rn" $db > dbs 
        cp dbs $db  
          echo "Record is deleted"
         cat $db;;           
        5)exit;;
        *);;
esac
done