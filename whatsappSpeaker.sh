 #!/bin/sh -x

adb shell input tap 594 127
for ((i=1; i<=100; i++)) 

do 
echo $i

sleep 3

adb shell input tap 128 1337

sleep 46

adb shell input tap 552 1110


done










