#!/bin/bash
url='http://localhost:8080/nifi/'
while ! curl -s $url >/dev/null; do
  echo -n '.'
  sleep 0.5
done
echo
echo $url
