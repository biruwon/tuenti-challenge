#!/bin/bash

# thanks to http://blog.gimco.es/2017/05/08/tuenti-challenge-7.html#5-ghost-in-the-http

for range in $(seq 0 13 3445); do
   # echo -n "$range"
    curl -v -k https://52.49.91.111:8443/ghost -r $range- >> ghost.b64
done
