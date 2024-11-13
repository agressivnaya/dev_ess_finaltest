#!/bin/bash
cd
mkdir TXT

# count .txt files in directory
x=0
for i in *.txt; do
((x++))
done

for i in *.txt; do
    cp $i TXT
    rm $i
done

echo "$x txt files moved"