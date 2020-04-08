#!/bin/bash
app="amex"
docker build -t ${app} .
docker run --rm -d -p 5000:5000 --name=${app} ${app}