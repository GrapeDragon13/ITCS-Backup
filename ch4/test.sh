#!/bin/sh
psets=('ch4_1.py' 'ch4_2.py' 'ch4_5.py' 'ch4_6.py' 'ch4_7.py' 'ch4_8.py' 'ch4_9.py' 'ch4_10.py' 'ch4_12.py' 'ch4_16.py' 'ch4_24.py' 'evenOdd.py' 'birthMonth.py' 'gradeBook.py' 'temperature.py')
echo 'updating testMe'
updateTestMe
for p in ${psets[@]}; do
    echo "testMe"  $p
    testMe $p
done

