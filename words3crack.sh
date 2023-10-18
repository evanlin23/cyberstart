#!/bin/bash

filename="words3.txt"

while IFS= read -r line
do
   ./strings3-x86 $line
   echo $line
done < "$filename"
