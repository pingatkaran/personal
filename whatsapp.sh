 #!/bin/sh -x


for ((i=1; i<=100; i++)) 

do 
echo $i
adb shell input tap 594 127

sleep 15

adb shell input tap 552 1110


done










