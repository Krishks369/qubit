#!/bin/bash

sudo rm output.csv
a=0
touch output.csv
   echo "IDS log"

while [ $a -lt 10 ]
do
  
   sudo timeout 5s src/kdd99extractor >> input.csv 2>errlog.txt
  
   /usr/bin/python3 mapper.py 

   
done
