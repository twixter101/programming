#!/bin/bash

read testcount

for (( i=0; i<$testcount; i++ )); do
    read cycle[$i]
    growth=1
    for (( j=0; j<${cycle[$i]}; j++ )); do
        if [ $(( $j%2 )) -eq 0 ]; then
            growth=$(( $growth*2 ))
        else
            (( growth++ ))
        fi
    done
    echo $growth
done