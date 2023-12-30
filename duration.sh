#!/usr/bin/env bash

coordinates=$1

X=$(curl -s https://www.timeanddate.com/eclipse/in/@"$coordinates"?iso=20240408 | grep "Totality:")

Y=$(echo $X | perl -pe 's/.*Totality\: <\/th><td>([0-9]+) minutes, ([0-9]+) second.*/$1 $2/g')

duration=$(echo $Y | awk '{ a=$1; b=$2; print a*60 + b }')

echo $duration
